import requests





def test_submission_endpoint():

    req = requests.post(
        "http://127.0.0.1:5000/submission",
        json={"submission": {
            "author": "kfortier",
            "resource": {
                "url": "https://stackoverflow.com/questions/927358/how-do-i-undo-the-most-recent-local-commits-in-git",
                "text": "How do I undo the most recent local commits in Git?",
                "type": "discussion",
            }

    }})
    print(req.content)

test_submission_endpoint()