"""
FitX Tracking Tools - Log workouts, meals, and retrieve progress summaries
"""

from typing import Dict, List
from datetime import datetime


def log_workout(exercise: str, duration: int, intensity: str, calories: int) -> Dict:
    """
    Log a completed workout session with details.
    
    Args:
        exercise: Type of exercise (e.g., 'cardio', 'strength training', 'yoga')
        duration: Duration in minutes
        intensity: Workout intensity ('low', 'moderate', 'high', 'very_high')
        calories: Estimated calories burned
    
    Returns:
        Dictionary with workout log entry and confirmation message
    
    Example:
        >>> log_workout("strength training", 45, "high", 350)
        {
            "timestamp": "2025-11-25T14:30:00",
            "exercise": "strength training",
            "duration_minutes": 45,
            "intensity": "high",
            "estimated_calories": 350,
            "status": "completed",
            "message": "Great job! You completed strength training for 45 minutes..."
        }
    """
    
    # Validate intensity
    valid_intensities = ['low', 'moderate', 'high', 'very_high']
    if intensity.lower() not in valid_intensities:
        intensity = 'moderate'  # Default to moderate if invalid
    
    # Generate motivational message based on workout
    messages = {
        'low': f'Nice work on your {exercise} session! Recovery and active rest are important too.',
        'moderate': f'Solid workout! {duration} minutes of {exercise} - you\'re building great habits.',
        'high': f'Excellent effort! That was an intense {duration}-minute {exercise} session.',
        'very_high': f'🔥 Incredible! {duration} minutes of very high intensity {exercise} - you crushed it!'
    }
    
    workout_log = {
        'timestamp': datetime.now().isoformat(),
        'exercise': exercise,
        'duration_minutes': duration,
        'intensity': intensity,
        'estimated_calories': calories,
        'status': 'completed',
        'message': messages.get(intensity, f'Great job completing your {exercise} workout!'),
        'stats': {
            'calories_per_minute': round(calories / duration, 1) if duration > 0 else 0,
            'total_active_time': duration,
            'intensity_level': intensity
        }
    }
    
    return workout_log


def log_meal(meal_type: str, food_items: List[str], calories: int) -> Dict:
    """
    Log a meal intake with nutritional information.
    
    Args:
        meal_type: Type of meal ('breakfast', 'lunch', 'dinner', 'snack')
        food_items: List of food items consumed
        calories: Total estimated calories for the meal
    
    Returns:
        Dictionary with meal log entry and confirmation message
    
    Example:
        >>> log_meal("breakfast", ["eggs", "toast", "avocado"], 450)
        {
            "timestamp": "2025-11-25T08:30:00",
            "meal_type": "breakfast",
            "items": ["eggs", "toast", "avocado"],
            "estimated_calories": 450,
            "status": "logged",
            "message": "Breakfast logged successfully..."
        }
    """
    
    # Validate meal type
    valid_meal_types = ['breakfast', 'lunch', 'dinner', 'snack']
    if meal_type.lower() not in valid_meal_types:
        meal_type = 'snack'  # Default to snack if invalid
    
    # Generate contextual messages
    meal_messages = {
        'breakfast': f'Breakfast logged! Starting the day with {len(food_items)} nutritious items.',
        'lunch': f'Lunch tracked! {len(food_items)} items providing midday fuel.',
        'dinner': f'Dinner logged! Ending the day with {len(food_items)} healthy choices.',
        'snack': f'Snack logged! {len(food_items)} items for sustained energy.'
    }
    
    # Determine meal size
    if calories < 200:
        size = 'light'
    elif calories < 500:
        size = 'moderate'
    elif calories < 800:
        size = 'substantial'
    else:
        size = 'large'
    
    meal_log = {
        'timestamp': datetime.now().isoformat(),
        'meal_type': meal_type.lower(),
        'items': food_items,
        'item_count': len(food_items),
        'estimated_calories': calories,
        'meal_size': size,
        'status': 'logged',
        'message': meal_messages.get(meal_type.lower(), 
                                     f'{meal_type.capitalize()} logged successfully!'),
        'tracking_note': f'Great job tracking! Consistency is key to reaching your goals.'
    }
    
    return meal_log


def get_progress_summary(days: int = 7) -> Dict:
    """
    Get a comprehensive fitness progress summary over a specified period.
    
    Args:
        days: Number of days to look back (default: 7 for weekly summary)
    
    Returns:
        Dictionary containing progress statistics and insights
    
    Example:
        >>> get_progress_summary(7)
        {
            "period": "Last 7 days",
            "workouts_completed": 5,
            "total_calories_burned": 2500,
            ...
        }
    """
    
    # In a real implementation, this would query a database
    # For now, returning mock data structure with realistic values
    
    # Calculate period description
    if days == 1:
        period_desc = "Today"
    elif days == 7:
        period_desc = "Last 7 days"
    elif days == 30:
        period_desc = "Last 30 days"
    else:
        period_desc = f"Last {days} days"
    
    # Mock data - in production, this would be actual user data
    workouts = 5 if days >= 7 else min(days, 2)
    total_calories = workouts * 350  # Average ~350 per workout
    avg_duration = 45
    
    # Calculate consistency percentage
    target_workouts = days if days <= 7 else 5  # Target 5 workouts per week
    consistency = min(round((workouts / target_workouts) * 100), 100)
    
    # Generate insights based on data
    insights = []
    
    if consistency >= 80:
        insights.append('🎉 Outstanding consistency! You\'re crushing your goals.')
    elif consistency >= 60:
        insights.append('💪 Great consistency! Keep up the excellent work.')
    elif consistency >= 40:
        insights.append('👍 Good progress! Try to maintain regular workout schedule.')
    else:
        insights.append('📈 Room for improvement! Consistency is key - let\'s get back on track.')
    
    if workouts > 0:
        insights.append(f'You burned an estimated {total_calories} calories through exercise.')
    
    if days >= 7:
        insights.append('Focus on progressive overload to continue seeing results.')
        insights.append('Don\'t forget recovery - rest days are when muscles grow!')
    
    # Goal progress (mock calculation)
    # In real app, this would compare to actual user goals
    goal_progress = min(consistency * 0.8, 100)  # Rough estimation
    
    summary = {
        'period': period_desc,
        'days_tracked': days,
        'workout_stats': {
            'workouts_completed': workouts,
            'target_workouts': target_workouts,
            'total_active_minutes': workouts * avg_duration,
            'average_workout_duration': avg_duration,
            'total_calories_burned': total_calories,
            'average_calories_per_workout': round(total_calories / workouts) if workouts > 0 else 0
        },
        'consistency': {
            'percentage': f'{consistency}%',
            'rating': 'Excellent' if consistency >= 80 else 
                     'Good' if consistency >= 60 else
                     'Fair' if consistency >= 40 else 'Needs Improvement',
            'workout_frequency': f'{workouts} workouts in {days} days'
        },
        'goal_progress': {
            'percentage': f'{round(goal_progress)}%',
            'status': 'On track' if goal_progress >= 60 else 
                     'Behind schedule' if goal_progress >= 40 else 'Needs attention',
            'message': 'Keep going! You\'re making progress toward your fitness goals.'
        },
        'insights': insights,
        'recommendations': [
            'Log all your workouts to track progress accurately',
            'Aim for at least 3-5 workouts per week',
            'Track your meals to optimize nutrition',
            'Increase intensity gradually for continued progress',
            'Celebrate small wins - consistency compounds!'
        ],
        'next_milestone': {
            'target': '10 consecutive workouts',
            'current': workouts,
            'remaining': max(0, 10 - workouts),
            'message': f'Only {max(0, 10 - workouts)} more workouts to hit your next milestone!'
        }
    }
    
    return summary
