const person = {
    firstName: 'John',
    lastName: 'Doe',
    age: 30,
    hobbies: ['music', 'movies', 'sports'],
    address: {
        street: '50 Main St',
        city: 'Boston',
        state: 'MA'
    }
}

console.log(person.firstName, person.lastName);
console.log(person.hobbies[1]);
console.log(person.address.city);

const { firstName, lastName, address : {city} } = person;
console.log(firstName);
console.log(city)

person.email = "john@gmail.com";
console.log(person);