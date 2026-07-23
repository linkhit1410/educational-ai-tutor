# Week 3 Debugging Reflection

## Purpose

Programming students often learn through debugging. Debugging is not only about fixing code; it is also a way for students to understand how Java works.

The purpose of this reflection is to think about how the AI tutor should support students when they encounter common Java errors.

---

## Common Java Debugging Scenarios

### 1. NullPointerException

A `NullPointerException` usually happens when a student tries to use an object reference that is currently `null`.

A helpful tutor should not immediately rewrite the student’s code. Instead, it should ask:

- Which line causes the error?
- Which object reference is being used on that line?
- Was the object created with `new`?
- Could the variable still be `null`?

This helps the student learn to connect the error message to object references and object creation.

---

### 2. ArrayIndexOutOfBoundsException

An `ArrayIndexOutOfBoundsException` happens when code tries to access an array index that does not exist.

A helpful tutor should guide the student to check:

- The array length.
- The index value.
- The loop condition.
- Whether the loop uses `<` instead of `<=`.

This helps students understand array bounds and loop behavior.

---

### 3. Cannot Find Symbol

A “cannot find symbol” error often means Java does not recognize a variable, method, or class name.

A helpful tutor should ask the student to check:

- Spelling and capitalization.
- Whether the variable was declared.
- Whether the method exists.
- Whether the code is using the correct object.
- Whether the needed class was imported.

This helps students understand scope, identifiers, and method calls.

---

### 4. Constructor Errors

Constructor errors are common for beginning Java students. Students may accidentally give a constructor a return type, forget that the constructor name must match the class name, or try to call a constructor with the wrong number of arguments.

A helpful tutor should remind students that:

- A constructor has the same name as the class.
- A constructor does not have a return type, not even `void`.
- Constructors are used to initialize new objects.
- If a constructor requires parameters, the object creation call must provide matching arguments.

The tutor should connect constructor errors back to object creation and initialization.

---

### 5. Inheritance Mistakes

Inheritance mistakes often happen when students misunderstand superclass and subclass relationships.

Students may think:

- A subclass automatically has direct access to all private superclass variables.
- Inheritance should be used for any two related classes.
- A superclass object can always be treated like a subclass object.
- The `extends` relationship means code is copied manually.

A helpful tutor should ask whether the relationship is really an is-a relationship. It should also remind students that superclass and subclass design should support reuse and class hierarchy organization.

---

### 6. Incorrect Method Overriding

Students may confuse method overriding with method overloading.

Overriding happens when a child class defines a method with the same signature as a method in the parent class. Overloading happens when methods have the same name but different parameter lists.

A helpful tutor should ask students to compare:

- Method name.
- Return type.
- Parameter number.
- Parameter types.
- Whether the method is in the same class or a subclass.

This helps students reason about which method Java will call.

---

## Debugging as a Learning Opportunity

Debugging can become a learning opportunity when the tutor helps the student reason through the problem instead of only giving the correction.

A weak debugging response says:

“Here is the fixed code.”

A stronger tutoring response says:

“Let’s look at the error message first. Which line does it point to? Which object or variable is being used on that line?”

This approach helps students practice a debugging process they can use again later.

---

## What the Tutor Should Do

For debugging questions, the tutor should:

- Ask for the error message if it is missing.
- Ask for the relevant code snippet if needed.
- Help identify the line where the problem occurs.
- Explain the concept behind the error.
- Suggest one next step at a time.
- Avoid rewriting the full solution immediately.
- Encourage the student to test their understanding.

---

## What the Tutor Should Avoid

For debugging questions, the tutor should avoid:

- Giving a full corrected program immediately.
- Skipping the student’s reasoning process.
- Assuming the cause without seeing the error or code.
- Providing too much code.
- Making the student dependent on the tutor for every fix.

---

## Reflection

Debugging is one of the most important places where an AI tutor can support learning. Many students feel frustrated when code does not work, but debugging can help them understand Java more deeply.

The tutor should treat bugs as evidence to investigate. It should help students ask: What does the error say? Where did it happen? What object, method, or variable is involved? What did I expect to happen? What actually happened?

This turns debugging from a correction task into a reasoning process.
