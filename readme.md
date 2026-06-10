# ActivityHub

ActivityHub is a simple command-line application that fetches and displays a GitHub user's recent public activity using the GitHub Events API.

Built as part of the GitHub User Activity project on roadmap.sh.

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
git clone https://github.com/Prakhar88/ActivityHub.git
cd ActivityHub
```

### Install Dependencies

```bash
pip install requests
```

## Usage

Run the program with a GitHub username:

```bash
python Main.py <github_username>
```

Example:

```bash
python Main.py torvalds
```

Output:

```text
Recent Work of torvalds on github:

• Pushed to torvalds/linux on branch master
• Created a branch in torvalds/linux
• Starred some-user/project
• Closed a pull request in another-user/repository
```

## Project Structure

```text
ActivityHub/
│
├── Main.py
├── README.md
└── requirements.txt
```

## API Endpoint

ActivityHub uses GitHub's public Events API:

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
* Requests Library
* GitHub REST API

## Roadmap.sh Project

This project was built as a solution to the GitHub User Activity challenge:

https://roadmap.sh/projects/github-user-activity

## License

This project is licensed under the MIT License.

## Author

Prakhar Srivastava
