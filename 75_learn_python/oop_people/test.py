import person
import children

p_1 = person.Person("Vio", 24)
print(p_1)
print('-')

# Test Getter
print('- Test Getter')
p_1_age = p_1.get_age()
print(p_1_age)
print('-')

# Test Setter
print('- Test Setter')
p_1.set_age(25)
print(p_1)
print('-')

# Test Inheritance
print('- Test Inheritance')
child_1 = children.Children("Ody", 3)
print(child_1)
child_1.print_size()
print(child_1.is_a)
print('meanwhile, Person 1')
p_1.print_size()
print(p_1.is_a)
print('-')
