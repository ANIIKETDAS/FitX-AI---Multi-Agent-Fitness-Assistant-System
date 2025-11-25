"""
FitX Shopping Tools - Search products across e-commerce platforms
"""

from typing import Dict


def search_fitness_equipment(query: str, category: str = "fitness") -> Dict:
    """
    Search for fitness equipment across multiple platforms (Amazon, Flipkart).
    
    Args:
        query: Equipment name (e.g., 'dumbbells', 'yoga mat', 'resistance bands')
        category: Equipment category (fitness, weights, cardio, yoga, accessories)
    
    Returns:
        Dictionary containing product recommendations from multiple platforms
    
    Example:
        >>> search_fitness_equipment("dumbbells", "weights")
        {
            "query": "dumbbells",
            "category": "weights",
            "platforms": {...}
        }
    """
    results = {
        'query': query,
        'category': category,
        'platforms': {
            'amazon': [
                {
                    'name': f'{query} - Premium Quality',
                    'price': '₹2,499',
                    'rating': '4.5/5',
                    'reviews': '1,234',
                    'features': [
                        'Durable construction',
                        'High-quality materials',
                        'Best seller',
                        'Fast delivery available'
                    ],
                    'link': f'amazon.in/search?q={query.replace(" ", "+")}'
                },
                {
                    'name': f'{query} - Budget Friendly',
                    'price': '₹999',
                    'rating': '4.2/5',
                    'reviews': '856',
                    'features': [
                        'Value for money',
                        'Good quality',
                        'Suitable for beginners',
                        'Prime delivery'
                    ],
                    'link': f'amazon.in/search?q={query.replace(" ", "+")}'
                }
            ],
            'flipkart': [
                {
                    'name': f'{query} - Top Rated',
                    'price': '₹1,899',
                    'rating': '4.4/5',
                    'reviews': '678',
                    'features': [
                        'Bestseller',
                        'Fast delivery',
                        'Great reviews',
                        'FlipkartAssured'
                    ],
                    'link': f'flipkart.com/search?q={query.replace(" ", "+")}'
                }
            ]
        },
        'recommendation': f'For {query}, the Premium Quality option offers the best value for long-term use. '
                          f'If budget is a concern, the Budget Friendly option is a great starting point.'
    }
    return results


def search_healthy_food(dietary_type: str, meal_type: str = "any") -> Dict:
    """
    Search for healthy food items on quick delivery platforms (Blinkit, Instamart).
    
    Args:
        dietary_type: Type of diet (e.g., 'high-protein', 'low-carb', 'vegan', 'keto')
        meal_type: Meal category (breakfast, lunch, dinner, snack, any)
    
    Returns:
        Dictionary containing food recommendations with nutritional info
    
    Example:
        >>> search_healthy_food("high-protein", "breakfast")
        {
            "dietary_type": "high-protein",
            "meal_type": "breakfast",
            "items": {...}
        }
    """
    
    # Customize recommendations based on dietary type
    if dietary_type.lower() in ['high-protein', 'high protein', 'protein']:
        items = [
            {
                'name': 'Organic Chicken Breast',
                'price': '₹350/kg',
                'delivery': '10 mins',
                'platform': 'Blinkit',
                'nutrition': {
                    'protein': '31g per 100g',
                    'fat': '3.6g per 100g',
                    'carbs': '0g',
                    'calories': '165 kcal per 100g'
                },
                'benefits': 'Lean protein source, great for muscle building'
            },
            {
                'name': 'Greek Yogurt (Plain)',
                'price': '₹180/500g',
                'delivery': '10 mins',
                'platform': 'Blinkit',
                'nutrition': {
                    'protein': '10g per 100g',
                    'fat': '5g per 100g',
                    'carbs': '4g per 100g',
                    'calories': '97 kcal per 100g'
                },
                'benefits': 'High protein, probiotics, versatile'
            },
            {
                'name': 'Eggs (Pack of 12)',
                'price': '₹84',
                'delivery': '10 mins',
                'platform': 'Blinkit',
                'nutrition': {
                    'protein': '6g per egg',
                    'fat': '5g per egg',
                    'carbs': '0.6g per egg',
                    'calories': '78 kcal per egg'
                },
                'benefits': 'Complete protein, affordable, versatile'
            }
        ]
    elif dietary_type.lower() in ['vegan', 'vegetarian']:
        items = [
            {
                'name': 'Tofu (Firm)',
                'price': '₹120/200g',
                'delivery': '10 mins',
                'platform': 'Blinkit',
                'nutrition': {
                    'protein': '8g per 100g',
                    'fat': '4g per 100g',
                    'carbs': '2g per 100g',
                    'calories': '76 kcal per 100g'
                },
                'benefits': 'Plant protein, iron, calcium'
            },
            {
                'name': 'Quinoa',
                'price': '₹280/500g',
                'delivery': '15 mins',
                'platform': 'Swiggy Instamart',
                'nutrition': {
                    'protein': '4.4g per 100g cooked',
                    'fat': '1.9g per 100g cooked',
                    'carbs': '21g per 100g cooked',
                    'calories': '120 kcal per 100g cooked'
                },
                'benefits': 'Complete protein, high fiber, gluten-free'
            },
            {
                'name': 'Mixed Beans',
                'price': '₹95/500g',
                'delivery': '10 mins',
                'platform': 'Blinkit',
                'nutrition': {
                    'protein': '7-9g per 100g',
                    'fiber': '6-8g per 100g',
                    'carbs': '20g per 100g',
                    'calories': '127 kcal per 100g'
                },
                'benefits': 'High protein, fiber, various minerals'
            }
        ]
    else:  # General healthy foods
        items = [
            {
                'name': 'Fresh Vegetables Mix',
                'price': '₹120/pack',
                'delivery': '10 mins',
                'platform': 'Blinkit',
                'nutrition': {
                    'fiber': 'High',
                    'vitamins': 'A, C, K',
                    'calories': 'Low (20-50 kcal per 100g)'
                },
                'benefits': 'Rich in vitamins, minerals, fiber'
            },
            {
                'name': 'Brown Rice',
                'price': '₹165/kg',
                'delivery': '15 mins',
                'platform': 'Swiggy Instamart',
                'nutrition': {
                    'protein': '2.6g per 100g cooked',
                    'fiber': '1.8g per 100g cooked',
                    'carbs': '23g per 100g cooked',
                    'calories': '111 kcal per 100g cooked'
                },
                'benefits': 'Complex carbs, fiber, minerals'
            },
            {
                'name': 'Mixed Nuts (Unsalted)',
                'price': '₹299/250g',
                'delivery': '10 mins',
                'platform': 'Blinkit',
                'nutrition': {
                    'protein': '6-7g per 30g',
                    'healthy fats': '14-16g per 30g',
                    'fiber': '2-3g per 30g',
                    'calories': '170-180 kcal per 30g'
                },
                'benefits': 'Healthy fats, protein, vitamin E'
            }
        ]
    
    results = {
        'dietary_type': dietary_type,
        'meal_type': meal_type,
        'items': items,
        'platforms': {
            'blinkit': 'Ultra-fast delivery (10 minutes) - Available in most major cities',
            'instamart': 'Quick delivery (15-20 minutes) - Wide selection'
        },
        'recommendation': f'For {dietary_type} diet, focus on whole, nutrient-dense foods. '
                          f'These items can be delivered quickly and support your fitness goals.'
    }
    
    return results


def search_athletic_wear(item_type: str, activity: str = "general") -> Dict:
    """
    Search for athletic wear and footwear on e-commerce platforms (Myntra, Amazon, Flipkart).
    
    Args:
        item_type: Type of clothing (e.g., 'running shoes', 'gym shorts', 'sports bra')
        activity: Activity type (running, gym, yoga, cycling, general)
    
    Returns:
        Dictionary containing clothing recommendations with features
    
    Example:
        >>> search_athletic_wear("running shoes", "running")
        {
            "item_type": "running shoes",
            "activity": "running",
            "recommendations": {...}
        }
    """
    results = {
        'item_type': item_type,
        'activity': activity,
        'recommendations': {
            'myntra': [
                {
                    'brand': 'Nike',
                    'name': f'{item_type} - Pro Series',
                    'price': '₹2,999',
                    'features': [
                        'Breathable mesh fabric',
                        'Moisture-wicking technology',
                        'Comfortable fit',
                        'Durable construction',
                        'Stylish design'
                    ],
                    'rating': '4.6/5',
                    'reviews': '2,145',
                    'sizes': 'S, M, L, XL, XXL',
                    'colors': '5 colors available',
                    'link': f'myntra.com/search?q={item_type.replace(" ", "+")}'
                },
                {
                    'brand': 'Puma',
                    'name': f'{item_type} - Active Fit',
                    'price': '₹1,999',
                    'features': [
                        'Flexible and stretchable',
                        'Durable fabric',
                        'Stylish athletic design',
                        'Good value for money',
                        'dryCELL technology'
                    ],
                    'rating': '4.4/5',
                    'reviews': '1,567',
                    'sizes': 'XS, S, M, L, XL',
                    'colors': '3 colors available',
                    'link': f'myntra.com/search?q={item_type.replace(" ", "+")}'
                },
                {
                    'brand': 'Adidas',
                    'name': f'{item_type} - Essential',
                    'price': '₹1,599',
                    'features': [
                        'Comfortable daily wear',
                        'Classic design',
                        'Good quality',
                        'Budget-friendly'
                    ],
                    'rating': '4.3/5',
                    'reviews': '987',
                    'sizes': 'S, M, L, XL',
                    'colors': '4 colors available',
                    'link': f'myntra.com/search?q={item_type.replace(" ", "+")}'
                }
            ],
            'amazon': [
                {
                    'brand': 'Adidas',
                    'name': f'{item_type} - Performance',
                    'price': '₹2,499',
                    'features': [
                        'Premium quality',
                        'Long-lasting',
                        'Professional grade',
                        'Amazon Prime delivery'
                    ],
                    'rating': '4.5/5',
                    'reviews': '3,421',
                    'link': f'amazon.in/search?q={item_type.replace(" ", "+")}'
                }
            ],
            'flipkart': [
                {
                    'brand': 'Reebok',
                    'name': f'{item_type} - Workout Ready',
                    'price': '₹1,799',
                    'features': [
                        'Great value',
                        'Comfortable',
                        'Good for workouts',
                        'Fast delivery'
                    ],
                    'rating': '4.2/5',
                    'reviews': '734',
                    'link': f'flipkart.com/search?q={item_type.replace(" ", "+")}'
                }
            ]
        },
        'buying_guide': {
            'fit': 'Choose true to size, consider trying before buying if possible',
            'material': 'Look for breathable, moisture-wicking fabrics',
            'purpose': f'Ensure product is designed for {activity}',
            'quality': 'Invest in good quality for frequently used items',
            'price': 'Balance budget with quality - mid-range often offers best value'
        },
        'recommendation': f'For {item_type} for {activity}, the Nike Pro Series offers premium quality, '
                          f'while Puma Active Fit provides excellent value. Choose based on your budget '
                          f'and how frequently you\'ll use them.'
    }
    
    return results
