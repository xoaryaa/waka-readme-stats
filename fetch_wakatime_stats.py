import requests
import os
import re

# Your WakaTime API key
WAKATIME_API_KEY = os.getenv('WAKATIME_API_KEY')
README_PATH = 'README.md'

def fetch_stats():
    headers = {'Authorization': f'Bearer {WAKATIME_API_KEY}'}
    response = requests.get('https://wakatime.com/api/v1/users/current/stats/last_7_days', headers=headers)
    response.raise_for_status()
    return response.json()

def update_readme(stats):
    with open(README_PATH, 'r') as file:
        readme_content = file.read()
    
    # Format stats (example format, adjust as needed)
    stats_content = f"""<!--START_SECTION:waka-->
- Total Time: {stats['data']['total_seconds'] / 3600} hours
- Most Used Language: {stats['data']['languages'][0]['name']}
<!--END_SECTION:waka-->"""
    
    # Replace the existing stats section in README
    new_readme_content = re.sub(r'<!--START_SECTION:waka-->.*<!--END_SECTION:waka-->', stats_content, readme_content, flags=re.DOTALL)
    
    with open(README_PATH, 'w') as file:
        file.write(new_readme_content)

if __name__ == "__main__":
    stats = fetch_stats()
    update_readme(stats)
