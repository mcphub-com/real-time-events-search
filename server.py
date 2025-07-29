import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/letscrape-6bRBa3QguO5/api/real-time-events-search'

mcp = FastMCP('real-time-events-search')

@mcp.tool()
def search_events(query: Annotated[str, Field(description='Search query / keyword.')],
                  date: Annotated[Literal['any', 'today', 'tomorrow', 'week', 'weekend', 'next_week', 'month', 'next_month', None], Field(description='Return events in a certain date / time period. Default: any Allowed values: any, today, tomorrow, week, weekend, next_week, month, next_month')] = None,
                  is_virtual: Annotated[Union[bool, None], Field(description='If true, only virtual events will be returned. Default: false')] = None,
                  start: Annotated[Union[int, float, None], Field(description='Number of results to skip (for pagination). Default: 0 Allowed values: positive integers Default: 0')] = None) -> dict: 
    '''Search for local public events in real-time. Supports filters and options as available on Google Events (i.e date and online filters).'''
    url = 'https://real-time-events-search.p.rapidapi.com/search-events'
    headers = {'x-rapidapi-host': 'real-time-events-search.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'date': date,
        'is_virtual': is_virtual,
        'start': start,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def event_details(event_id: Annotated[str, Field(description='The ID of the event to fetch (i.e. event_id field of an event).')]) -> dict: 
    '''Get the details of a specific event by Event ID (i.e. *event_id* field of an event).'''
    url = 'https://real-time-events-search.p.rapidapi.com/event-details'
    headers = {'x-rapidapi-host': 'real-time-events-search.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'event_id': event_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
