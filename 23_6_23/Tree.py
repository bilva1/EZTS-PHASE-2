families={'charley':{'sam':{'Boxy','Rosy'},
                     'Nila':{'pepsi'}},
          'Devi':{'Tommy':{'Tony'},
                  'Timmy':{'Hamster'},
                  'Tammy':{'Hamster'}
                 },
          'Carlos':{'Diego':{'cat'},
                    'Ferret':{'Fox'}}
        }
for parent, children in families.items():
          print(f"{parent} has {len(children)} kids:")
          print(f"{', and '.join([str(child) for child in [*children]])}")
