# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: ExpenseSplit
def validate_date(date_str):
    """Validate date string in DD/MM/YYYY or YYYY-MM-DD format."""
    if not isinstance(date_str, str) or len(date_str.strip()) == 0:
        return None, "Invalid date format"
    
    try:
        day_part = int(date_str[:2])
        month_part = int(date_str[3:5])
        year_part = int(date_str[6:])
        
        if not (1 <= day_part <= 31 and 1 <= month_part <= 12):
            return None, "Invalid date values"
            
        import datetime
        
        try:
            valid_date = datetime.date(year_part, month_part, day_part)
            return valid_date.isoformat(), None
        except ValueError:
            return None, "Date doesn't exist in calendar"
    except (ValueError, IndexError):
        return None, "Invalid date format"

def validate_amount(amount_str):
    """Validate amount string to be a positive number."""
    if not isinstance(amount_str, str) or len(amount_str.strip()) == 0:
        return None, "Invalid amount format"
    
    try:
        amount = float(amount_str.strip().replace(',', '.'))
        if amount <= 0:
            return None, "Amount must be positive"
        return amount, None
    except ValueError:
        return None, "Invalid amount format"

def validate_participant(participant_str):
    """Validate participant name."""
    if not isinstance(participant_str, str) or len(participant_str.strip()) == 0:
        return None, "Empty participant name"
    
    if ',' in participant_str:
        participants = [p.strip() for p in participant_str.split(',')]
        if any(not p for p in participants):
            return None, "Invalid participant format"
        return participants, None
    
    if not participant_str[0].isalpha():
        return None, "Participant name must start with letter"
    
    if len(participant_str) > 50:
        return None, "Participant name too long"
    
    return [participant_str.strip()], None

def validate_category(category_str):
    """Validate category string."""
    valid_categories = ['Food', 'Transport', 'Entertainment', 'Shopping', 'Bills', 'Other']
    
    if not isinstance(category_str, str) or len(category_str.strip()) == 0:
        return None, "Empty category"
    
    normalized = category_str.strip().title()
    if normalized in valid_categories:
        return [normalized], None
    
    if ',' in category_str and len([c.strip() for c in category_str.split(',')]) > 1:
        categories = [c.strip().title() for c in category_str.split(',')]
        invalid = [c for c in categories if c not in valid_categories]
        if invalid:
            return None, f"Invalid category: {', '.join(invalid)}"
        
        return categories, None
    
    return None, f"Unknown category: {category_str}"

def process_transaction(raw_input):
    """Process a transaction string and return validated data or error message."""
    if not raw_input.strip():
        return {"error": "Empty input"}
    
    try:
        parts = raw_input.split(';')
        
        date_part = validate_date(parts[0].strip())
        amount_part = validate_amount(parts[1].strip())
        participant_part = validate_participant(parts[2]) if len(parts) > 2 else None
        
        if any(part[1] is not None for part in [date_part, amount_part]):
            return {"error": f"Validation failed: {date_part[1]} or {amount_part[1]}" if date_part[1] else amount_part[1]}
        
        category_part = validate_category(parts[3].strip()) if len(parts) > 3 else ('Other', None)
        
        if category_part[1]:
            return {"error": category_part[1]}
        
        return {
            "date": date_part[0],
            "amount": amount_part[0],
            "participants": participant_part[0] if participant_part and not participant_part[1] else ['Unknown'],
            "category": category_part[0]
        }
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}

# Example usage
print(process_transaction("25/03/2024;150.50;Alice,Bob;Food"))
