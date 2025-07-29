# Real-Time Events Search MCP Server

## Overview

The Real-Time Events Search MCP Server is a powerful tool designed to provide fast, reliable, and comprehensive search capabilities for events worldwide in real-time. It covers a broad spectrum of event types, including concerts, sports matches, workshops, festivals, movies, and more. This server is ideal for applications that require up-to-the-minute information about public events, whether local or online.

## Key Features

- **Real-Time Search**: Instantly access current events across various categories and locations.
- **Comprehensive Data**: Supports a wide range of events including concerts, sports, workshops, festivals, and movies.
- **High Performance**: Optimized for quick response times and reliability, ensuring you get the data you need when you need it.

## Getting Started

To utilize the Real-Time Events Search MCP Server, you can use the following tools:

### Tools

#### Search Events

- **Description**: This tool allows you to search for local public events in real-time. It supports various filters and options akin to those available on Google Events, such as date and online filters.
- **Parameters**:
  - **query**: The search query or keyword.
  - **date**: Filter events by a specific date or time period (e.g., today, tomorrow, week, weekend, etc.).
  - **is_virtual**: Boolean option to filter only virtual events.
  - **start**: For pagination, specify the number of results to skip.

#### Event Details

- **Description**: Retrieve detailed information about a specific event using its Event ID.
- **Parameters**:
  - **event_id**: The unique identifier for the event you want to retrieve details about.

## Response Structure

All responses from the server are in JSON format and include the following fields:

- **status**: Indicates if the request was successful ("OK") or if there was an error ("ERROR").
- **request_id**: A unique identifier for the request.
- **data**: Contains the requested data if the status is "OK".
- **error**: If the status is "ERROR", this field provides details about the error, including an error message and code.

## Rate Limiting

The server applies rate limiting to ensure fair usage and system stability:

- **Request Limits**: Each subscription plan defines the maximum number of requests allowed per month.
- **Rate Limit Headers**: Responses include headers that provide information on the remaining requests and reset time.

## Error Handling

The server uses HTTP status codes to indicate the nature of any issues encountered:

- **400 Bad Request**: The request is malformed or missing required parameters.
- **403 Forbidden**: Access is denied due to invalid credentials or subscription status.
- **404 Not Found**: The requested resource could not be found.
- **429 Too Many Requests**: The rate limit has been exceeded.
- **5XX Server Error**: Indicates server-side issues.

Implement error handling in your applications to manage these responses effectively.

## Conclusion

The Real-Time Events Search MCP Server is an essential tool for developers and businesses seeking to integrate real-time event data into their applications. With its robust features and user-friendly interface, it provides a seamless experience for discovering and accessing event information. 

For further assistance or inquiries, please reach out to our support team.