import random
from acme import Product


'''
Now you can represent your inventory - let's use these classes and write an
acme_report.py module to generate random products and print a summary of them.
For the purposes of these functions we will only use the `Product` class.

Your module should include two functions:

- `generate_products()` should generate a given number of products (default
  30), randomly, and return them as a list
- `inventory_report()` takes a list of products, and prints a "nice" summary

For the purposes of generation, "random" means uniform - all possible values
should vary uniformly across the following possibilities:

- `name` should be a random adjective from `['Awesome', 'Shiny', 'Impressive',
  'Portable', 'Improved']` followed by a space and then a random noun from
  `['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']`, e.g. `'Awesome Anvil'`
  and `Portable Catapult'` are both possible
- `price` and `weight` should both be from 5 to 100 (inclusive and independent,
  and remember - they're integers!)
- `flammability` should be from 0.0 to 2.5 (floats)
'''


adj = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
noun = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', 'Box']


def generate_products(n=30):
    '''`generate_products()` should generate a given number of products (default
        30), randomly, and return them as a list
    '''

    # Instantiate empty products list
    products = []

    # Generate random products and append to products list
    for _ in range(n):

        # Create random product names
        adj_choice = random.choice(adj)
        noun_choice = random.choice(noun)
        product_name = f'{adj_choice} {noun_choice}'

        # Create individual products
        product = Product(name=product_name,
                          price=random.randint(5, 101),
                          weight=random.randint(5, 101),
                          flammability=random.uniform(0.0, 2.5),
                          )

        # Append product to products list
        products.append(product)

    return products


def inventory_report(products):
    '''takes a list of products, and prints a "nice" summary'''

    # Instantiate empty set
    inventory = set()
    weight_total = 0
    price_total = 0
    flammability_total = 0

    # Loop through products
    for product in products:
        inventory.add(product.name)
        weight_total += product.weight
        price_total += product.price
        flammability_total = product.flammability

    # Get average price, weight, and flammability
    weight_average = weight_total / len(products)
    price_average = price_total / len(products)
    flammability_average = flammability_total / len(products)

    # Generate the report
    print('\nInventory Report')
    print('-------------------------------\n')
    print('Number of unique products:', len(products))
    print(f'Average weight: {weight_average: .2f}')
    print(f'Average price: {price_average: .2f}')
    print(f'Average flammability: {flammability_average: .2f}\n')


if __name__ == '__main__':
    inventory_report(generate_products())
