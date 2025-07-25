# 🕸️ Simple Web Scraping Agent
hiii
A powerful, interactive web scraping agent built with Python that leverages Firecrawl's comprehensive web scraping capabilities. This agent provides an intelligent interface for extracting, analyzing, and researching web content with multiple specialized tools.

## ✨ Features

- **Interactive Agent Interface**: Natural language queries for web scraping tasks
- **Multiple Scraping Methods**: Single page scraping, site mapping, full crawling, and more
- **Intelligent Content Extraction**: AI-powered content analysis and summarization
- **Real-time Crawl Monitoring**: Check status of long-running crawl operations
- **Search & Research**: Built-in search capabilities and deep research tools
- **LLM-Optimized Output**: Generate LLM-friendly text files from scraped content

## 🛠️ Available Tools

The agent comes equipped with 8 specialized Firecrawl tools:

| Tool | Description |
|------|-------------|
| `firecrawl_scrape` | Scrape content from a single webpage |
| `firecrawl_map` | Generate a sitemap of a website's structure |
| `firecrawl_crawl` | Perform comprehensive crawling of entire websites |
| `firecrawl_check_crawl_status` | Monitor the progress of crawl operations |
| `firecrawl_search` | Search for specific content across websites |
| `firecrawl_extract` | Extract structured data from web pages |
| `firecrawl_deep_research` | Conduct in-depth research on topics using web data |
| `firecrawl_generate_llmstxt` | Convert scraped content to LLM-optimized format |

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- UV package manager
- Firecrawl API key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/debasmitaas/Web-Scraping-Agent.git
   cd Web-Scraping-Agent
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```

3. **Set up environment variables**
   ```bash
   # Create a .env file and add your Firecrawl API key and LLM API key (Gemini in this case)
   echo "FIRECRAWL_API_KEY=your_api_key_here" > .env
   echo "GEMINI_API_KEY=your_api_key_here" > .env
   ```

### Running the Agent

```bash
uv run main.py
```

The agent will start and display available tools, then wait for your input.

## 💡 Usage Examples

### Basic Website Analysis
```
User Input: what is on https://nextjs.org/docs website?
```

### Deep Dive into Documentation
```
User Input: tell me more about API reference
```

### Site Mapping
```
User Input: map the structure of https://example.com
```

### Content Search
```
User Input: search for "authentication" on https://docs.example.com
```

### Research Mode
```
User Input: research the latest trends in web development frameworks
```



