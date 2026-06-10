# ActivityHub

ActivityHub is a lightweight command-line application that fetches and displays a GitHub user's recent public activity using the GitHub Events API.

Built as part of the roadmap.sh GitHub User Activity project.

## Features

* Fetches recent public GitHub activity for any user
* Displays activities in a clean, readable format
* Supports multiple GitHub event types:

  * PushEvent
  * CreateEvent
  * DeleteEvent
  * WatchEvent
  * ForkEvent
  * IssuesEvent
  * IssueCommentEvent
  * PullRequestEvent
  * PullRequestReviewEvent
  * PullRequestReviewCommentEvent
  * ReleaseEvent
  * PublicEvent
* Handles invalid usernames
* Handles network-related errors
* Simple command-line interface

## Installation

### Clone the Repository

```bash
git clone https://github.com/Prakhar88/Github-Activity-API.git
cd Github-Activity-API
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install requests
```

## Usage

Run the application from the terminal:

```bash
python ActivityHub.py <github_username>
```

Example:

```bash
python ActivityHub.py torvalds
```

## Example Output

```text
Recent Work of torvalds on github:

• Pushed to torvalds/linux on branch master
• Created a branch in torvalds/linux
• Starred some-user/project
• Closed a pull request in another-user/repository
```

## Project Structure

```text
Github-Activity-API/
│
├── ActivityHub.py
├── requirements.txt
└── README.md
```

## API Endpoint

This project uses GitHub's public Events API:

```text
https://api.github.com/users/<username>/events
```

## Error Handling

The application handles:

* Invalid GitHub usernames (404 Not Found)
* Network connection issues
* Missing command-line arguments
* Unexpected API responses

## Technologies Used

* Python 3
* Requests
* GitHub REST API

## Roadmap.sh Project

https://roadmap.sh/projects/github-user-activity

## Author

Prakhar Srivastava

## License

This project is licensed under the MIT License.
