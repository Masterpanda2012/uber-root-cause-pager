# uber-root-cause-pager
Root cause pager: routes one page to the team whose service failed first (Zero DevOps scenario)

## Setup
python3 -m venv .venv && source .venv/bin/activate
python summarize.py data/<outage>.csv
