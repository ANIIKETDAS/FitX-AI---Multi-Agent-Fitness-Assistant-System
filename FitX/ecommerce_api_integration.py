"""
Real E-commerce API Integration for FitX AI
Integrates with Amazon, Flipkart, Blinkit, Swiggy Instamart APIs
"""

import os
import requests
import json
from typing import Dict, List, Any, Optional
from datetime import datetime
import hashlib
import hmac
import base64
from urllib.parse import quote, urlencode

# ==================== AMAZON PRODUCT ADVERTISING API ====================
class AmazonProductAPI:
   ## NOT ABLE TO GET AMAZON AFFILIATE API WORKING CURRENTLY DUE TO SIGNING ISSUES ##
    def __init__(self):
        self.access_key = os.getenv('AMAZON_ACCESS_KEY')
        self.secret_key = os.getenv('AMAZON_SECRET_KEY')
        self.associate_tag = os.getenv('AMAZON_ASSOCIATE_TAG')
        self.host = "webservices.amazon.in"
        self.region = "eu-west-1"
        self.marketplace = "www.amazon.in"
        
    def search_items(self, keywords: str, category: str = "All") -> Dict:
        """Search for items using PA-API"""
        endpoint = f"https://{self.host}/paapi5/searchitems"
        
        payload = {
            "Keywords": keywords,
            "Resources": [
                "Images.Primary.Large",
                "ItemInfo.Title",
                "ItemInfo.Features",
                "Offers.Listings.Price"
            ],
            "SearchIndex": category,
            "PartnerTag": self.associate_tag,
            "PartnerType": "Associates",
            "Marketplace": self.marketplace
        }
        
        headers = self._get_headers(payload)
        
        try:
            response = requests.post(endpoint, json=payload, headers=headers)
            response.raise_for_status()
            return self._parse_amazon_response(response.json())
        except requests.exceptions.RequestException as e:
            return {"error": str(e), "source": "amazon"}
    
    def _get_headers(self, payload: Dict) -> Dict:
        """Generate AWS Signature Version 4 headers"""
        # Implementation of AWS SigV4 signing

        return {
            "Content-Type": "application/json",
            "X-Amz-Target": "com.amazon.paapi5.v1.ProductAdvertisingAPIv1.SearchItems",
            "Content-Encoding": "amz-1.0"
        }
    
    def _parse_amazon_response(self, data: Dict) -> List[Dict]:
        """Parse Amazon API response"""
        if 'SearchResult' not in data:
            return []
        
        items = []
        for item in data.get('SearchResult', {}).get('Items', []):
            parsed_item = {
                'platform': 'Amazon',
                'asin': item.get('ASIN'),
                'title': item.get('ItemInfo', {}).get('Title', {}).get('DisplayValue'),
                'price': self._extract_price(item),
                'rating': item.get('CustomerReviews', {}).get('StarRating', {}).get('Value'),
                'image': item.get('Images', {}).get('Primary', {}).get('Large', {}).get('URL'),
                'url': item.get('DetailPageURL'),
                'features': item.get('ItemInfo', {}).get('Features', {}).get('DisplayValues', [])
            }
            items.append(parsed_item)
        return items
    
    def _extract_price(self, item: Dict) -> str:
        """Extract price from complex Amazon structure"""
        try:
            price_info = item.get('Offers', {}).get('Listings', [{}])[0].get('Price', {})
            amount = price_info.get('Amount')
            currency = price_info.get('Currency', 'INR')
            return f"{currency} {amount}"
        except:
            return "Price not available"


# ==================== FLIPKART AFFILIATE API ====================
class FlipkartAPI:
    """
    Flipkart Affiliate API

    """
    ##NOT ABLE TO TEST DUE TO LACK OF AFFILIATE ACCOUNT##
    def __init__(self):
        self.affiliate_id = os.getenv('FLIPKART_AFFILIATE_ID')
        self.affiliate_token = os.getenv('FLIPKART_AFFILIATE_TOKEN')
        self.base_url = "https://affiliate-api.flipkart.net/affiliate"
        
    def search_products(self, query: str, category: str = "all") -> List[Dict]:
        """Search products on Flipkart"""
        endpoint = f"{self.base_url}/search/json"
        
        params = {
            'query': query,
            'resultCount': 10
        }
        
        headers = {
            'Fk-Affiliate-Id': self.affiliate_id,
            'Fk-Affiliate-Token': self.affiliate_token
        }
        
        try:
            response = requests.get(endpoint, params=params, headers=headers)
            response.raise_for_status()
            return self._parse_flipkart_response(response.json())
        except requests.exceptions.RequestException as e:
            return {"error": str(e), "source": "flipkart"}
    
    def get_product_details(self, product_id: str) -> Dict:
        """Get detailed product information"""
        endpoint = f"{self.base_url}/product/json"
        
        params = {'id': product_id}
        headers = {
            'Fk-Affiliate-Id': self.affiliate_id,
            'Fk-Affiliate-Token': self.affiliate_token
        }
        
        try:
            response = requests.get(endpoint, params=params, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}
    
    def _parse_flipkart_response(self, data: Dict) -> List[Dict]:
        """Parse Flipkart API response"""
        products = []
        for product in data.get('products', []):
            parsed = {
                'platform': 'Flipkart',
                'product_id': product.get('productId'),
                'title': product.get('productBaseInfoV1', {}).get('title'),
                'price': product.get('productBaseInfoV1', {}).get('flipkartSellingPrice', {}).get('amount'),
                'mrp': product.get('productBaseInfoV1', {}).get('maximumRetailPrice', {}).get('amount'),
                'discount': product.get('productBaseInfoV1', {}).get('discountPercentage'),
                'rating': product.get('productBaseInfoV1', {}).get('rating', {}).get('average'),
                'image': product.get('productBaseInfoV1', {}).get('imageUrls', [{}])[0].get('400x400'),
                'url': product.get('productBaseInfoV1', {}).get('productUrl'),
                'in_stock': product.get('productBaseInfoV1', {}).get('inStock')
            }
            products.append(parsed)
        return products


# ==================== BLINKIT API  ====================
class BlinkitAPI:
    """
    Blinkit does NOT have public API

    This is a MOCK implementation showing structure
    """
    def __init__(self):
        self.base_url = "https://blinkit.com"  # No official API
        self.session = requests.Session()
        # Note: Real implementation would need authentication tokens
        
    def search_products(self, query: str, location: str = "default") -> List[Dict]:
        """
        WARNING: Blinkit has no public API
        This is a mock/placeholder
        Real implementation options:
        1. Scrape website (check ToS first)
        2. Use Selenium/Playwright for automation
        3. Contact Blinkit for API access
        """
        # Mock data structure
        return self._get_mock_blinkit_data(query)
    
    def _get_mock_blinkit_data(self, query: str) -> List[Dict]:
        """Return mock data structure"""
        return [
            {
                'platform': 'Blinkit',
                'name': f'{query} - Fresh',
                'price': '₹199',
                'discount': '10% off',
                'delivery_time': '10 mins',
                'image': 'https://example.com/image.jpg',
                'in_stock': True,
                'note': 'Mock data - Blinkit has no public API'
            }
        ]


# ==================== SWIGGY INSTAMART API (UNOFFICIAL) ====================
class SwiggyInstamartAPI:
    """
    Swiggy Instamart does NOT have public API
    
    """
    def __init__(self):
        self.base_url = "https://www.swiggy.com/instamart"  # No official API
        
    def search_products(self, query: str, location_id: str = None) -> List[Dict]:
        """
        WARNING: No public API available
        Options:
        1. Scraping (check legality and ToS)
        2. Browser automation
        3. Contact Swiggy for partnership
        """
        return self._get_mock_instamart_data(query)
    
    def _get_mock_instamart_data(self, query: str) -> List[Dict]:
        """Return mock data structure"""
        return [
            {
                'platform': 'Swiggy Instamart',
                'name': f'{query} - Premium',
                'price': '₹249',
                'discount': '15% off',
                'delivery_time': '15-20 mins',
                'image': 'https://example.com/image.jpg',
                'in_stock': True,
                'note': 'Mock data - Swiggy has no public API'
            }
        ]




# ==================== UNIFIED E-COMMERCE INTERFACE ====================
class UnifiedEcommerceAPI:
    """
    Unified interface for all e-commerce platforms
    Handles fallbacks and aggregation
    """
    def __init__(self):
        self.amazon = AmazonProductAPI()#Currently NO WORKING DUE TO SIGNING ISSUES
        self.flipkart = FlipkartAPI()
        self.blinkit = BlinkitAPI()  # Mock
        self.instamart = SwiggyInstamartAPI()  # Mock
        
        
    def search_all_platforms(self, query: str, platforms: List[str] = None) -> Dict[str, List[Dict]]:
        """
        Search across multiple platforms
        Returns aggregated results
        """
        if platforms is None:
            platforms = ['amazon', 'flipkart']  # Only real APIs by default
        
        results = {}
        
        if 'amazon' in platforms:
            try:
                results['amazon'] = self.amazon.search_items(query)
            except Exception as e:
                results['amazon'] = {'error': str(e)}
        
        if 'flipkart' in platforms:
            try:
                results['flipkart'] = self.flipkart.search_products(query)
            except Exception as e:
                results['flipkart'] = {'error': str(e)}
        
        if 'blinkit' in platforms:
            results['blinkit'] = self.blinkit.search_products(query)
            results['blinkit_note'] = 'Mock data - no public API'
        
        if 'instamart' in platforms:
            results['instamart'] = self.instamart.search_products(query)
            results['instamart_note'] = 'Mock data - no public API'
        
        return results
    
    def compare_prices(self, product_name: str) -> List[Dict]:
        """Compare prices across platforms"""
        all_results = self.search_all_platforms(product_name)
        
        # Flatten and sort by price
        all_products = []
        for platform, products in all_results.items():
            if isinstance(products, list):
                all_products.extend(products)
        
        # Sort by price (implement proper price parsing)
        return all_products
    
    def get_best_deal(self, product_name: str) -> Dict:
        """Find the best deal across all platforms"""
        products = self.compare_prices(product_name)
        
        # Logic to determine "best" (lowest price, fastest delivery, etc.)
        if products:
            return min(products, key=lambda x: self._extract_numeric_price(x.get('price', '9999')))
        return {}
    
    def _extract_numeric_price(self, price_string: str) -> float:
        """Extract numeric price from string"""
        try:
            import re
            numbers = re.findall(r'\d+\.?\d*', str(price_string))
            return float(numbers[0]) if numbers else float('inf')
        except:
            return float('inf')


# ==================== INTEGRATION WITH FITX AGENTS ====================

def integrate_with_fitness_agent():
    """
    Example of integrating with the main FitX agent
    """
    ecommerce = UnifiedEcommerceAPI()
    
    # Update the tool functions in fitness_agent.py
    def search_fitness_equipment_real(query: str, category: str = "fitness") -> str:
        """Real API version"""
        results = ecommerce.search_all_platforms(query, platforms=['amazon', 'flipkart'])
        return json.dumps(results, indent=2)
    
    def search_healthy_food_real(dietary_type: str, meal_type: str = "any") -> str:
        """Real API version (mock for Blinkit/Instamart)"""
        # Use mock for now since no public API
        results = {
            'blinkit': ecommerce.blinkit.search_products(f"{dietary_type} {meal_type}"),
            'instamart': ecommerce.instamart.search_products(f"{dietary_type} {meal_type}"),
            'note': 'These platforms do not have public APIs. Consider web scraping or partnerships.'
        }
        return json.dumps(results, indent=2)
    
    def search_athletic_wear_real(item_type: str, activity: str = "general") -> str:
        """Real API version"""
        results = ecommerce.search_all_platforms(item_type, platforms=['amazon', 'flipkart'])
        return json.dumps(results, indent=2)
    
    return {
        'search_fitness_equipment': search_fitness_equipment_real,
        'search_healthy_food': search_healthy_food_real,
        'search_athletic_wear': search_athletic_wear_real
    }




if __name__ == "__main__":
    # Test the integration
    print("E-commerce API Integration for FitX AI")
    print("="*60)
    
    # Example usage
    ecommerce = UnifiedEcommerceAPI()
    
    # Search for fitness equipment
    print("\nSearching for 'dumbbells'...")
    results = ecommerce.search_all_platforms('dumbbells', platforms=['amazon', 'flipkart'])
    print(json.dumps(results, indent=2))
    
    # Find best deal
    print("\nFinding best deal for 'yoga mat'...")
    best_deal = ecommerce.get_best_deal('yoga mat')
    print(json.dumps(best_deal, indent=2))
