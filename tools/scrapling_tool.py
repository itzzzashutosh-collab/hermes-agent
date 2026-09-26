#!/usr/bin/env python3
"""Scrapling tool: High-performance adaptive web scraping and anti-bot bypass for Hermes.
Provides structured data extraction for competitor pricing, raw material spot rates, and tender monitoring.
"""

import json
import logging
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)

SCRAPLING_SCHEMA = {
    "type": "function",
    "function": {
        "name": "scrapling_scrape",
        "description": (
            "Scrape web pages with anti-bot bypass and element extraction using Scrapling. "
            "Use for competitor paint price monitoring, raw material chemical rates, and tender portals."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string",
                    "description": "The target website URL to scrape."
                },
                "css_selector": {
                    "type": "string",
                    "description": "Optional CSS selector to extract specific elements (e.g. '.price-box', 'h1', 'table')."
                },
                "extract_text": {
                    "type": "boolean",
                    "description": "Whether to extract clean visible text. Default is true.",
                    "default": True
                },
                "stealth": {
                    "type": "boolean",
                    "description": "Whether to use StealthyFetcher to bypass Cloudflare / anti-bot protection. Default is false.",
                    "default": False
                }
            },
            "required": ["url"]
        }
    }
}

def _check_scrapling_reqs() -> bool:
    try:
        import scrapling
        return True
    except ImportError:
        return False

def scrapling_scrape(
    url: str,
    css_selector: Optional[str] = None,
    extract_text: bool = True,
    stealth: bool = False
) -> str:
    """Execute scraping with Scrapling Fetcher or StealthyFetcher."""
    if not url or not url.strip():
        return json.dumps({"error": "URL parameter is required and cannot be empty."})

    target_url = url.strip()
    if not (target_url.startswith("http://") or target_url.startswith("https://")):
        target_url = "https://" + target_url

    try:
        from scrapling import Fetcher
        
        if stealth:
            try:
                from scrapling import StealthyFetcher
                page = StealthyFetcher.get(target_url, timeout=20)
            except Exception as e:
                logger.warning(f"StealthyFetcher failed or unavailable ({e}); falling back to standard Fetcher.")
                page = Fetcher.get(target_url, timeout=15)
        else:
            page = Fetcher.get(target_url, timeout=15)

        status_code = getattr(page, "status", 200)
        
        # Extract title
        title_list = page.css("title::text").extract()
        title = title_list[0].strip() if title_list else ""

        # Extract selected elements if specified
        selected = []
        if css_selector and css_selector.strip():
            elements = page.css(css_selector.strip()).extract()
            selected = [e.strip() for e in elements[:30] if e and e.strip()]

        # Extract main text
        extracted_text = ""
        if extract_text:
            paragraphs = page.css("p::text, h1::text, h2::text, h3::text, li::text, td::text").extract()
            clean_lines = [p.strip() for p in paragraphs if p and len(p.strip()) > 3]
            extracted_text = "\n".join(clean_lines[:100])
            if len(extracted_text) > 8000:
                extracted_text = extracted_text[:8000] + "… [truncated]"

        result = {
            "status": "SUCCESS",
            "url": target_url,
            "http_status": status_code,
            "title": title,
            "selector_used": css_selector,
            "selected_count": len(selected),
            "selected_elements": selected,
            "text_preview": extracted_text[:1500] if extracted_text else ""
        }
        return json.dumps(result, ensure_ascii=False)

    except Exception as exc:
        logger.error(f"Scrapling scrape failed for {target_url}: {exc}")
        return json.dumps({
            "status": "ERROR",
            "url": target_url,
            "error": str(exc)
        }, ensure_ascii=False)

from tools.registry import registry

registry.register(
    name="scrapling_scrape",
    toolset="web",
    schema=SCRAPLING_SCHEMA,
    check_fn=_check_scrapling_reqs,
    handler=lambda args, **kw: scrapling_scrape(
        url=args.get("url", ""),
        css_selector=args.get("css_selector"),
        extract_text=args.get("extract_text", True),
        stealth=args.get("stealth", False)
    ),
    emoji="🕷️"
)
