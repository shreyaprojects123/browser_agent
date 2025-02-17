# agent.py
from playwright.sync_api import sync_playwright, TimeoutError
import time
import logging

class BrowserAgent:
    def __init__(self):
        try:
            self.playwright = sync_playwright().start()
            self.browser = self.playwright.firefox.launch(
                headless=False,
                slow_mo=100  # Increased delay between actions
            )
            self.context = self.browser.new_context(
                viewport={'width': 1280, 'height': 800}
            )
            self.page = self.context.new_page()
            logging.info("Browser initialized successfully")
        except Exception as e:
            logging.error(f"Failed to initialize browser: {str(e)}")
            raise

    def execute_prompt(self, prompt):
        try:
            if "amazon.com" in prompt.lower() and "computer" in prompt.lower():
                return self._handle_amazon_search()
            return "Prompt not recognized"
        except Exception as e:
            logging.error(f"Error in execute_prompt: {str(e)}")
            raise

    def _handle_amazon_search(self):
        try:
            logging.info("Starting Amazon search")
            
            # Navigate to Amazon with a more basic wait strategy
            self.page.goto("https://www.amazon.com", wait_until="domcontentloaded")
            
            # Wait for and find the search box
            search_box_selector = "input[name='field-keywords']"
            self.page.wait_for_selector(search_box_selector, timeout=10000)
            
            # Clear the search box first
            self.page.click(search_box_selector)
            self.page.fill(search_box_selector, "")
            
            # Type and search
            self.page.fill(search_box_selector, "computer")
            self.page.press(search_box_selector, "Enter")
            
            # Wait for search results with multiple fallback selectors
            result_selectors = [
                "div[data-component-type='s-search-result']",
                ".s-result-item",
                ".s-search-results"
            ]
            
            for selector in result_selectors:
                try:
                    self.page.wait_for_selector(selector, timeout=5000)
                    logging.info(f"Found results with selector: {selector}")
                    break
                except TimeoutError:
                    continue
            
            # Add a small delay to ensure results are loaded
            time.sleep(2)
            
            results = []
            products = self.page.query_selector_all("div[data-component-type='s-search-result']")
            
            if not products:
                products = self.page.query_selector_all(".s-result-item")
            
            for i, product in enumerate(products[:5]):
                try:
                    title_elem = product.query_selector("h2 span") or product.query_selector(".a-text-normal")
                    price_elem = product.query_selector(".a-price .a-offscreen") or product.query_selector(".a-price")
                    
                    title = title_elem.inner_text() if title_elem else "No title found"
                    price = price_elem.inner_text() if price_elem else "No price found"
                    
                    results.append({
                        "title": title,
                        "price": price
                    })
                    
                    if len(results) >= 5:
                        break
                except Exception as e:
                    logging.error(f"Error processing product {i}: {str(e)}")
                    continue

            logging.info(f"Found {len(results)} results")
            return results
            
        except Exception as e:
            logging.error(f"Error in Amazon search: {str(e)}")
            raise

    def __del__(self):
        try:
            if hasattr(self, 'context'):
                self.context.close()
            if hasattr(self, 'browser'):
                self.browser.close()
            if hasattr(self, 'playwright'):
                self.playwright.stop()
        except Exception as e:
            logging.error(f"Error in cleanup: {str(e)}")