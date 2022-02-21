def filter_if(condition: bool, expression, iterable):
    """
    Allows you to filter an iterable based on a condition. If the condition is met, the filter is applied
    :param condition: Condition to apply the filter
    :param expression: Expression that represents the filter to apply
    :param iterable: Iterable that contains the elements to filter
    :return: Iterable applying the filters as appropriate
    """
    if condition:
        return filter(expression, iterable)
    return iterable
