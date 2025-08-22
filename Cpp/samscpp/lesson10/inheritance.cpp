/**
 * Sam's C++ 9th edition - Lesson 10 - Inheritance
 *
 * Here's how we do inheritance in C++.
 * Some Notes to keep in mind coming from other languages:
 * 1. C++ does support multiple inheritance.
 * 2. C++ does not have a "super" keyword.
 * 3. C++ does not have interfaces, but we can use abstract classes with solely pure virtual functions
 *    to achieve a similar effect (still requires inheritance though).
*/

#include <iostream>

class Fish {
    // protected members can be accessed by derived classes
protected:
    int number_of_fins{2};
    bool is_freshwater_fish{false};

public:
    void swim() {
        if (is_freshwater_fish) {
            std::cout << "swim in lake" << std::endl;
        } else {
            std::cout << "swim in ocean" << std::endl;
        }
    }
};

/**
 * Tune inherits from Fish using the ":" syntax.
 *
 * C++ has a couple difference types of inheritance:
 * 1. Public (common) - all public and protected members keep their access levels (what client code sees).
 * 2. Private - all public and protected members become private (e.g., outside code cannot access Fish members).
 *    note, without the "public" keyword, inheritance is private by default.
 * 3. Protected - all public and protected members become protected
 *    (e.g., only tuna and derived classes can access Fish members, but not outside code).
 */
class Tuna : public Fish {
    // Private by default (don't need to use the "private" keyword)
    // only Tuna can access this member
    int deliciousness_rating{10};

public:
    Tuna() {
        is_freshwater_fish = false;
    }
};

/** Implicit private inheritance
 * Note: if another class inherits from this, it cannot access Fish members.
 */
class Carp : Fish {
public:
    Carp() {
        is_freshwater_fish = true;
    }
};

class Goldfish : public Fish {
public:
    std::string gold_fish_classification;

    Goldfish() {
        is_freshwater_fish = true;
        number_of_fins = 4;
    }

    /**
     *  The 'explicit' keyword prevents implicit conversions
     *  e.g., Goldfish g = "common"; would be an error, but Goldfish g("Oranda"); is fine.
     */
    explicit Goldfish(const std::string &classification = "common") {
        is_freshwater_fish = true;
        number_of_fins = 4;
        gold_fish_classification = classification;
    }
};

/**
 * This class inherits from Goldfish, which in turn inherits from Fish.
 * It's also final, meaning no other class can inherit from Lionhead.
 */
class Lionhead final : public Goldfish {
    int head_width;

public:
    /**
     * Base class initialization using list initialization syntax.
     *
     */
    Lionhead() : Goldfish("lionhead") {
        // Base class constructor are called before the derived class constructor
        head_width = number_of_fins * 2;
    }

    /**
     * Overriding base class method.
     * If the child class method has the same signature as the parent class, it overrides it.
     * If we want to call the parent class method, we can do so using the scope resolution operator (::).
     */
    void swim() {
        Fish::swim();
        std::cout << "with while roaring like a lion!" << std::endl;
    }

    int get_head_width() const {
        return head_width;
    }
};


// Multiple inheritance
class Animal {
public:
    void walk() {
        std::cout << "walk on land" << std::endl;
    }
};

class Platypus : public Fish, public Animal {
public:
    Platypus() {
        is_freshwater_fish = true;
    }

    void swim() {
        std::cout << "I'm a platypus, I can swim!" << std::endl;
        Fish::swim();
    }

    void walk_and_swim() {
        walk();
        swim();
    }
};

int main() {
    // // simple inheritance and protected members
    // Tuna tuna = Tuna();
    // tuna.swim(); // swim in ocean
    // tuna.is_freshwater_fish = true; // Error: cannot access protected members

    // // Nested inheritance and overriding base classes
    // Goldfish ranchu = Goldfish("Ranchu");
    // Lionhead lionhead = Lionhead();
    // std::cout << ranchu.gold_fish_classification << std::endl; // Ranchu
    // std::cout << lionhead.gold_fish_classification << std::endl; // lionhead
    // lionhead.swim(); // swim in lake

    // Multiple inheritance
    Platypus perry = Platypus();
    perry.walk_and_swim(); // walk on land, swim in lake
}
