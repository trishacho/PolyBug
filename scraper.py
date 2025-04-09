import requests
import csv
import sys

def fetch_issues(bug_type, num_issues):
    github_api_url = "https://api.github.com/search/issues"
    params = {
        "q": f"label:bug state:closed {bug_type}",
        "per_page": min(num_issues, 100)
    }
    headers = {"Accept": "application/vnd.github.v3+json"}

    all_issues = []
    page = 1
    while len(all_issues) < num_issues:
        params["page"] = page
        response = requests.get(github_api_url, params=params, headers=headers)
        if response.status_code == 200:
            issues = response.json().get("items", [])
            if not issues:
                break
            all_issues.extend(issues)
        else:
            print("Error fetching data:", response.status_code)
            break
        page += 1
    return all_issues[:num_issues]

def get_fix_commit(issue_url):
    headers = {"Accept": "application/vnd.github.v3+json"}
    timeline_url = issue_url + "/timeline"
    response = requests.get(timeline_url, headers=headers)
    if response.status_code == 200:
        events = response.json()
        for event in events:
            if event.get("event") == "referenced" and "commit_id" in event:
                return event["commit_id"]
    return "N/A"

def save_to_csv(issues, filename="github_bugs_with_fixes.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "URL", "Repository", "Created At", "Fix Commit"])
        for issue in issues:
            fix_commit = get_fix_commit(issue["url"])
            writer.writerow([issue["title"], issue["html_url"], issue["repository_url"], issue["created_at"], fix_commit])
    print(f"Saved {len(issues)} issues to {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 scraper.py <bug_type> <number_of_issues>")
        sys.exit(1)
    
    bug_type = sys.argv[1]
    num_issues = int(sys.argv[2])
    
    issues = fetch_issues(bug_type, num_issues)
    if issues:
        save_to_csv(issues)
