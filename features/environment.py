import os
import shutil
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()

# Environment details
BASE_URL = os.getenv("BASE_URL")

# Playwright settings
RECORD_VIDEO = os.getenv("PLAYWRIGHT_RECORD_VIDEO")
HEADLESS = True if os.getenv("PLAYWRIGHT_SETTINGS_HEADLESS") == 'Y' else False


def before_all(context):
    # insert script to run data prep to setup test data sql

    # deletes recorded videos from previous run
    if os.path.exists("./videos"):
        for filename in os.listdir("./videos"):
            filepath = os.path.join("./videos", filename)
            try:
                shutil.rmtree(filepath)
            except OSError:
                os.remove(filepath)

    # starts playwright
    context.playwright = sync_playwright().start()

    # set browser to be used
    # set if browser should run as headless or not
    context.browser = context.playwright.chromium.launch(headless=HEADLESS, args=["--start-maximized"])

    # Create Browser Context
    # Turns on and off recording of test video
    if RECORD_VIDEO == 'Y':
        context.browser_context = context.browser.new_context(
            base_url=BASE_URL,
            no_viewport=True,
            record_video_dir='./videos',
            record_video_size={
                                "width": 1920,
                                "height": 1080
                            }
        )
    else:
        context.browser_context = context.browser.new_context(
            base_url=BASE_URL
        )

    # generates a zip file that can be opened in Playwrights Trace Viewer
    # https://playwright.dev/python/docs/trace-viewer
    context.browser_context.tracing.start(screenshots=True, snapshots=True, sources=True)

    # creates a new page in browser
    context.page = context.browser_context.new_page()

def after_step(context, step):

    # generate screenshots only if step failed
    if step.status == "failed":
        context.page.screenshot(
            path="./screenshots/" + context.scenario.name + str(step.line) + '.png'
        )

def after_all(context):
    # insert script to run data cleanup to setup test data sql

    # generate and save the zip file
    context.browser_context.tracing.stop(path="trace.zip")

    # methods to close playwright
    context.browser_context.close()
    context.browser.close()
    context.playwright.stop()
