#!/usr/bin/env -S uv run
# /// script
# dependencies = [
#     "requests<3",
# ]
# ///
"""
Called by GH Actions when the nightly build fails.

This reports an error to the #nightly-build-failures Slack channel.
"""

import os

import requests


if "SLACK_WEBHOOK_URL" in os.environ:
    print("Reporting to #nightly-build-failures slack channel")
    response = requests.post(
        os.environ["SLACK_WEBHOOK_URL"],
        json={
            "text": (
                f"A Nightly build failed. See https://github.com/"
                f"{os.environ['GITHUB_REPOSITORY']}/actions/runs/{os.environ['GITHUB_RUN_ID']}"
            ),
        },
        timeout=30,
    )

    print("Slack responded with:", response)

else:
    print(
        "Unable to report to #nightly-build-failures slack channel because SLACK_WEBHOOK_URL is not set"
    )
