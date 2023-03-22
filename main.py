import re

def solve_equation(equation):
    # Clean up the equation by removing whitespace and rearrange it so that all the terms are on one side
    equation = equation.replace(' ', '')
    equation = equation.replace('-', '+-')
    sides = equation.split('=')
    left_side = sides[0]
    right_side = sides[1]
    left_side_terms = left_side.split('+')
    right_side_terms = right_side.split('+')
    for term in right_side_terms:
        if term.startswith('-'):
            left_side_terms.append(term)
        else:
            left_side_terms.append('-' + term)
    # Combine like terms
    coefficients = {}
    for term in left_side_terms:
        if 'x' in term:
            if term.startswith('-'):
                coefficient = -1
            elif term == 'x':
                coefficient = 1
            else:
                coefficient = int(re.findall(r'\d+', term)[0])
            coefficients['x'] = coefficients.get('x', 0) + coefficient
        else:
            coefficients['constant'] = coefficients.get('constant', 0) + int(term)
    # Solve for x
    x = -coefficients['constant'] / coefficients['x']
    # Return the solution as a string with all the steps
    steps = []
    steps.append(equation)
    steps.append('Cleaning up the equation:')
    steps.append(equation.replace('=', ' = '))
    steps.append('Rearranging the equation so that all the terms are on one side:')
    steps.append(left_side + '- ' + right_side + ' = 0')
    steps.append('Combining like terms:')
    steps.append(str(coefficients['x']) + 'x + ' + str(coefficients['constant']) + ' = 0')
    steps.append('Solving for x:')
    steps.append('x = ' + str(x))
    return '\n'.join(steps)

