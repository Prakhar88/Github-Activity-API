import requests
import sys

def get_github_activity(username):
    url=f"https://api.github.com/users/{username}/events"
    try:
        response=requests.get(url,timeout=30)
        if response.status_code==200:
            recent_events=response.json()
            print(f"Recent Work of {username} on github:")
            for event in recent_events:
                event_type = event["type"]
                repo = event["repo"]["name"]
                print("•",end="")
                if event_type == "PushEvent":
                    branch = event["payload"]["ref"].split("/")[-1]
                    print(f"Pushed to {repo} on branch {branch}")

                elif event_type == "CreateEvent":
                    ref_type = event["payload"].get("ref_type", "something")
                    print(f"Created a {ref_type} in {repo}")

                elif event_type == "DeleteEvent":
                    ref_type = event["payload"].get("ref_type", "something")
                    print(f"Deleted a {ref_type} in {repo}")

                elif event_type == "WatchEvent":
                    print(f"Starred {repo}")

                elif event_type == "ForkEvent":
                    print(f"Forked {repo}")

                elif event_type == "IssuesEvent":
                    action = event["payload"].get("action", "updated")
                    print(f"{action.capitalize()} an issue in {repo}")

                elif event_type == "IssueCommentEvent":
                    print(f"Commented on an issue in {repo}")

                elif event_type == "PullRequestEvent":
                    action = event["payload"].get("action", "updated")
                    print(f"{action.capitalize()} a pull request in {repo}")

                elif event_type == "PullRequestReviewEvent":
                    print(f"Reviewed a pull request in {repo}")

                elif event_type == "PullRequestReviewCommentEvent":
                    print(f"Commented on a pull request in {repo}")

                elif event_type == "ReleaseEvent":
                    print(f"Published a release in {repo}")

                elif event_type == "PublicEvent":
                    print(f"Made {repo} public")

                else:
                    print(f"{event_type} in {repo}")
            
        elif response.status_code==404:
            print("Error 404: User not found")
        else:
            print(f"Error {response.status_code}:Google it, idk what this is")
        
        return None
    except requests.exceptions.RequestException as e:
        print("Network Error: ",e)
        return  None


if __name__ =="__main__":
    if len(sys.argv) != 2:
        print("Usage: python Main.py <github_username>")
        sys.exit(1)
    username = sys.argv[1]
    get_github_activity(username)
