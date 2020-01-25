import re

test_cases = ['''Date 1 :  12/11/18           Date 2: 01/01/19'''] 

# Create a dictionary to convert from month names to numbers (e.g. Jan = 01)
month_dict = dict(jan='01', feb='02', mar='03', apr='04', may='05', jun='06', jul='07', aug='08', sep='09',
                  oct='10', nov='11', dec='12')


def word_to_num(string):
    """
    This function converts a string to lowercase and only accepts the first three letter.
    This is to prepare a string for month_dict
    Example:
        word_to_num('January') -> jan
    """

    s = string.lower()[:3]
    return(month_dict[s])


def date_converter(line):
    """
    This function extracts dates in every format from text and converts them to YYYYMMDD.
    Example:
        date_converter("It was the May 1st, 2009") -> 20090501
    """
    results = []
    day = '01'
    month = '01'
    year = '1900'
    # If format is MM/DD/YYYY or M/D/YY or some combination
    regex = re.search('([0]?\d|[1][0-2])[/-]([0-3]?\d)[/-]([1-2]\d{3}|\d{2})', line)
    # If format is DD Month YYYY or D Mon YY or some combination, also matches if no day given
    month_regex = re.search(
        '([0-3]?\d)\s*(Jan(?:uary)?(?:aury)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|June?|July?|Aug('
        '?:ust)?|Sept?(?:ember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?(?:emeber)?).?,?\s([1-2]\d{3})',
        line)
    # If format is Month/DD/YYYY or Mon/D/YY or or Month DDth, YYYY or some combination
    rev_month_regex = re.search(
        '(Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|June?|July?|Aug(?:ust)?|Sept?(?:ember)?|Oct('
        '?:ober)?|Nov(?:ember)?|Dec(?:ember)?).?[-\s]([0-3]?\d)(?:st|nd|rd|th)?[-,\s]\s*([1-2]\d{3})',
        line)
    rev_th_regex = re.search(
        '([0-3]?\d)(?:st|nd|rd|th)? (Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|June?|July?|Aug(?:ust)?|Sept?(?:ember)?|Oct('
        '?:ober)?|Nov(?:ember)?|Dec(?:ember)?).?[-,\s]\s*([1-2]\d{3})',
        line)
    # If format is any combination of just Month or Mon and YY or YYYY
    no_day_regex = re.search(
        '(Jan(?:uary)?(?:aury)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|June?|July?|Aug(?:ust)?|Sept?('
        '?:ember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?(?:emeber)?).?,?[\s]([1-2]\d{3}|\d{2})',
        line)
    # If format is MM/YYYY or M YYYY or some combination
    no_day_digits_regex = re.search('([0]?\d|[1][0-2])[/\s]([1-2]\d{3})', line)
    # If format only contains a year. If year is written alone it must be in form YYYY
    year_only_regex = re.search('([1-2]\d{3})', line)
    if regex:
        return(regex)
    elif month_regex:
         return(month_regex)
    elif rev_month_regex:
        return(rev_month_regex)
        
    elif rev_th_regex:
        return(rev_th_regex)
    elif no_day_regex:
        return(no_day_regex)
    elif no_day_digits_regex:
        return(no_day_digits_regex)
    elif year_only_regex:
        return(year_only_regex)
    # Make sure all variables have correct number, add zeros if necessary
test_run = [date_converter(w) for w in test_cases]
print(test_run)