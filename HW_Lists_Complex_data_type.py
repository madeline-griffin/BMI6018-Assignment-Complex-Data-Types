{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "43c61910",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Assignment 3\n"
     ]
    }
   ],
   "source": [
    "\"\"\"BMI 6018 Fall 2026\n",
    "\n",
    "Instructions: \n",
    "\n",
    "For this assignment, please return all answers as variables in your\n",
    ".py  (or .ipynb) file. You will quickly note that you will need to find answers outside the\n",
    "class lectures. This is not an accident! You will need to become professionally\n",
    "comfortable with looking things up via the python docs and google. \n",
    "\n",
    "Ensure that all variables are labelled according to the example. IE the answer\n",
    "to problem 1 part c should be labelled \"one_c\". While all questions are answerable\n",
    "with a single line of code, you are free to use helper variables so long as they\n",
    "are helpfully/informatively named. \n",
    "\n",
    "I should be able to open your .py (or .ipynb) file and run it without errors. I will **not** be \n",
    "debugging your code for you. If your file does not run, it will **not** be graded. \n",
    "If you are unsure if your file will run, open up a chpc terminal and test it there.\n",
    "\n",
    "For this assignment, please only use base python files types. That is: there \n",
    "should be no import calls in your file save my use of sys at the end.\n",
    "\n",
    "Example Problem\n",
    "\n",
    "0.a Create a list of strings\n",
    "0.b Using a str method, capitalize one of the elements in the list using a slice\n",
    "0.c Coerce one character of one element of the list to display as a hex\n",
    "\n",
    "zero_a = ['first','second','third','fourth','fifth']\n",
    "zero_b = zero_a[1].upper()\n",
    "zero_c = hex(ord(zero_a[1][1]))\n",
    "\n",
    "#Problem 1: Lists, Sets and Coersion\n",
    "\n",
    "1.a Create a list of integers no fewer than 10 items from 0 to 9.\n",
    " .b Add 3 to the 5th indexed element\n",
    " .c Coerce all elements in the list to floats using list comprehension\n",
    " .d Coerce the list to a set\n",
    " .e Using a method, append int 10 to the set\n",
    " .f Using a method, pop an item from the set\n",
    " .g Using a length counting function, count the number of items in the set\n",
    " .h Check if the number of items in the set is the same as the \n",
    "    number of items in the list\n",
    " .i Coerce the set to a list and use the \"+\" operator combine the list to the list from 1.a\n",
    " .j Coerce 1.i to a set\n",
    " .k Count the number of elements in the 1.j\n",
    "\n",
    "\n",
    "\n",
    "Problem 2: Dictionary woes\n",
    "\n",
    "2.a Combine the three sample dictionaries (given below) into a nested dictionary (nested in programming means joined), named \n",
    "    two_a, ensure the key names are the same as the dictionary names.\n",
    " .b Using keys, retrieve the Dango's name from 2.a\n",
    " .c Using keys, update the value of Mochi's year to 2018. This should not be a variable\n",
    "    and should simply update 2.a.\n",
    " .d Manually create a dictionary that has a single level and contains each patient\n",
    "    as the key and the year as the value. Set Mochi's year to 2019.'\n",
    " .e Coerce the keys of 2.d into a list\n",
    " .f Coerce the values of 2.d into a list\n",
    " .g Use the zip function to combine 2.e and 2.f into a dictionary again\n",
    "\n",
    "\n",
    "two_patient_dictionary_kinoko = {\n",
    "  \"name\" : \"Kinoko\",\n",
    "  \"year\" : 2021\n",
    "}\n",
    "two_patient_dictionary_dango = {\n",
    "  \"name\" : \"Dango\",\n",
    "  \"year\" : 2019\n",
    "}\n",
    "two_patient_dictionary_mochi  = {\n",
    "  \"name\" : \"Mochi\",\n",
    "  \"year\" : 2020\n",
    "}\n",
    "\n",
    "\n",
    "\n",
    "Problem 3: Set combinations\n",
    "\n",
    "Given the predefined sets below and using set methods\n",
    "3.a Is set E a subset of set A\n",
    " .b Is set E a strict subset of set A\n",
    " .c Create a set that is the intersection of set A and set B\n",
    " .d Create a set that is the union of sets C, D and E\n",
    " .e add 9 to the set\n",
    " .f Using == compare this set to the list in one_a\n",
    " .g Explain why they are not the same. What would you need to change if you\n",
    "    wanted this to be True?\n",
    " \n",
    "\n",
    "three_setA = {1,2,3,4,5}\n",
    "three_setB = {2,3,4,5,6}\n",
    "three_setC = {3,5,7,9}\n",
    "three_setD = {2,4,6,8}\n",
    "three_setE = {1,2,3,4}\n",
    "\n",
    "\n",
    "\n",
    "Problem 4: Changing variable types\n",
    "\n",
    "For each step you will modify a variable, then append the type of the variable\n",
    "to a list. Do not recreate the list variable, it should be a running list of \n",
    "types.\n",
    "\n",
    "4.a Create a variable of type int with the value of 8\n",
    " .b Create an empty list \n",
    " .c Using type(), add the type of 4.a to this list\n",
    " .d Add 0.39 to 4.c\n",
    " .e append the type of 0.39 to the list\n",
    " .f exponentiate to the -10, ie: 4.d^-10,(hint there might be an artihmetic operator to do so) round it to no \n",
    "    decimal places, and append to list.\n",
    " .g append the type to the list\n",
    " \n",
    " \n",
    "Problem 5: More variable type changes\n",
    "\n",
    "Continue from where you left off in Problem 4.\n",
    "\n",
    "5.a Manually create a dictionary where the values are items in the list from where we left in \n",
    "    problem 4, and the keys should be their index in the list. Print the dictionary.\n",
    " .b Add 300 and coerce it into a string\n",
    " .c append the type to the list\n",
    " .d slice the string up to the 2nd element\n",
    " .e append the type to the list\n",
    " .f use list comprehension to convert this into a new list of integers\n",
    " .g append the type to the list\n",
    " .h append the type of three_setA to the list\n",
    "\"\"\"\n",
    "\n",
    "#Start your assignment here\n",
    "print(\"Assignment 3\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "367710fd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\n"
     ]
    }
   ],
   "source": [
    "# Problem 1: Lists, Sets and Coercion\n",
    "\n",
    "# 1.a Create a list of integers no fewer than 10 items from 0 to 9.\n",
    "one_a= [0,1,2,3,4,5,6,7,8,9]\n",
    "print(one_a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "14c81602-c285-4eee-a7e8-904457114564",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 1, 2, 3, 4, 8, 6, 7, 8, 9]\n"
     ]
    }
   ],
   "source": [
    "# 1.b Add 3 to the 5th indexed element (index 5).\n",
    "one_a[5] = one_a[5] + 3\n",
    "one_b= one_a\n",
    "print(one_b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "6614bfdd-3ac4-4f21-af5f-78a5f8e9ea6c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.0, 1.0, 2.0, 3.0, 4.0, 8.0, 6.0, 7.0, 8.0, 9.0]\n"
     ]
    }
   ],
   "source": [
    "# 1.c Coerce all elements in the list to floats using list comprehension.\n",
    "one_c = [float(x) for x in one_a]\n",
    "print(one_c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "685339d2-f348-4ac7-a328-5a366a7f0f28",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{0.0, 1.0, 2.0, 3.0, 4.0, 6.0, 7.0, 8.0, 9.0}\n"
     ]
    }
   ],
   "source": [
    "# 1.d Coerce the list to a set.\n",
    "one_d = set(one_c)\n",
    "print(one_d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "de0d10c5-c83a-4372-97f4-b9204b32968f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{0.0, 1.0, 2.0, 3.0, 4.0, 6.0, 7.0, 8.0, 9.0, 10}\n"
     ]
    }
   ],
   "source": [
    "# 1.e Using a method, append int 10 to the set.\n",
    "one_d.add(10)\n",
    "one_e=one_d\n",
    "print(one_e)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "cb36c314-6886-4f6f-86d4-0b8a6bd6ed97",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{0.0, 1.0, 2.0, 3.0, 4.0, 6.0, 7.0, 8.0, 9.0}\n"
     ]
    }
   ],
   "source": [
    "# 1.f Using a method, pop an item from the set.\n",
    "one_e.remove(10)\n",
    "one_f=one_e\n",
    "print(one_f)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "18946363-570c-410a-84c4-ffab356ec069",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "9\n"
     ]
    }
   ],
   "source": [
    "# 1.g Using a length counting function, count the number of items in the set.\n",
    "one_g = len(one_f)\n",
    "print(one_g)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "1abde68a-3756-4fe9-b68b-06fddfe8b15a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "# 1.h Check if the number of items in the set is the same as the number of items in the list.\n",
    "one_h = len(one_f) == len(one_a)\n",
    "print(one_h)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "db657c7e-bda1-4ff6-a49a-ddc7fd1af48e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.0, 1.0, 2.0, 3.0, 4.0, 6.0, 7.0, 8.0, 9.0, 0, 1, 2, 3, 4, 8, 6, 7, 8, 9]\n"
     ]
    }
   ],
   "source": [
    "# 1.i Coerce the set to a list and use \"+\" to combine it with the list from 1.a.\n",
    "one_i = list(one_f) + one_a\n",
    "print(one_i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "aac959e4-9cd9-46d5-b465-5679ea02a58a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{0.0, 1.0, 2.0, 3.0, 4.0, 6.0, 7.0, 8.0, 9.0}\n"
     ]
    }
   ],
   "source": [
    "# 1.j Coerce 1.i to a set.\n",
    "one_j = set(one_i)\n",
    "print(one_j)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "35fffeef-15f6-472f-b690-26ab5a35be14",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "9\n"
     ]
    }
   ],
   "source": [
    "# 1.k Count the number of elements in 1.j.\n",
    "one_k = len(one_j)\n",
    "print(one_k)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "e2f35992-c394-4011-b620-34ff3e956f6b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Problem 2: Dictionary woes\n",
    "two_patient_dictionary_kinoko = {\n",
    "    \"name\": \"Kinoko\",\n",
    "    \"year\": 2021\n",
    "}\n",
    "two_patient_dictionary_dango = {\n",
    "    \"name\": \"Dango\",\n",
    "    \"year\": 2019\n",
    "}\n",
    "two_patient_dictionary_mochi = {\n",
    "    \"name\": \"Mochi\",\n",
    "    \"year\": 2020\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "20db81f9-254f-40ad-8b92-7121490ef091",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'two_patient_dictionary_kinoko': {'name': 'Kinoko', 'year': 2021}, 'two_patient_dictionary_dango': {'name': 'Dango', 'year': 2019}, 'two_patient_dictionary_mochi': {'name': 'Mochi', 'year': 2020}}\n"
     ]
    }
   ],
   "source": [
    "# 2.a Combine the three sample dictionaries (given below) into a nested dictionary (nested in programming means joined), \n",
    "# named two_a, ensure the key names are the same as the dictionary names.\n",
    "two_a = {\n",
    "    \"two_patient_dictionary_kinoko\": two_patient_dictionary_kinoko,\n",
    "    \"two_patient_dictionary_dango\": two_patient_dictionary_dango,\n",
    "    \"two_patient_dictionary_mochi\": two_patient_dictionary_mochi\n",
    "}\n",
    "print(two_a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "327a628e-97db-41cb-802e-0ce705fc0eec",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Dango\n"
     ]
    }
   ],
   "source": [
    "# 2.b Using keys, retrieve Dango's name from 2.a.\n",
    "two_b = two_a[\"two_patient_dictionary_dango\"][\"name\"]\n",
    "print(two_b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "04245569-f978-43a7-ad6c-612261f82df8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2018\n"
     ]
    }
   ],
   "source": [
    "# 2.c Using keys, update the value of Mochi's year to 2018 (updates 2.a directly).\n",
    "two_a[\"two_patient_dictionary_mochi\"][\"year\"] = 2018\n",
    "two_c = two_a[\"two_patient_dictionary_mochi\"][\"year\"]\n",
    "print(two_c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "54004787-97d6-4146-b6b0-faf7a2bd56a2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Kinoko': 2021, 'Dango': 2019, 'Mochi': 2019}\n"
     ]
    }
   ],
   "source": [
    "# 2.d Manually create a single-level dictionary of patient -> year, with Mochi's year set to 2019.\n",
    "two_d = {\n",
    "    \"Kinoko\": 2021,\n",
    "    \"Dango\": 2019,\n",
    "    \"Mochi\": 2019\n",
    "}\n",
    "print(two_d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "3e63e6f8-38e9-4b5a-837c-8dba421f4fb8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Kinoko', 'Dango', 'Mochi']\n"
     ]
    }
   ],
   "source": [
    "# 2.e Coerce the keys of 2.d into a list.\n",
    "two_e = list(two_d.keys())\n",
    "print(two_e)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "2172f940-7757-4d44-8fdc-bbad4e2fca2c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2021, 2019, 2019]\n"
     ]
    }
   ],
   "source": [
    "# 2.f Coerce the values of 2.d into a list.\n",
    "two_f = list(two_d.values())\n",
    "print(two_f)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "28eef8a1-a72f-435c-89bd-fe7161c60b16",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Kinoko': 2021, 'Dango': 2019, 'Mochi': 2019}\n"
     ]
    }
   ],
   "source": [
    "# 2.g Use zip to combine 2.e and 2.f into a dictionary again.\n",
    "two_g = dict(zip(two_e, two_f))\n",
    "print(two_g)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "41ace53d-c6cc-4aad-98e6-691b6789c4cc",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Problem 3: Set combinations\n",
    "three_setA = {1, 2, 3, 4, 5}\n",
    "three_setB = {2, 3, 4, 5, 6}\n",
    "three_setC = {3, 5, 7, 9}\n",
    "three_setD = {2, 4, 6, 8}\n",
    "three_setE = {1, 2, 3, 4}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "a1735ba8-bac9-4519-aae7-c0be98275046",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "# 3.a Is set E a subset of set A?\n",
    "three_a = three_setE.issubset(three_setA)\n",
    "print(three_a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "100195f0-add1-4526-b45b-e3c66e53112c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "# 3.b Is set E a strict (proper) subset of set A?\n",
    "three_b = three_setE < three_setA\n",
    "print(three_b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "458e5997-d1c3-4f00-9435-3e3bfef0cc91",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{2, 3, 4, 5}\n"
     ]
    }
   ],
   "source": [
    "# 3.c Intersection of set A and set B.\n",
    "three_c = three_setA.intersection(three_setB)\n",
    "print(three_c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "9b14e8e9-ba30-4354-b937-bac2cb8eb0fa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1, 2, 3, 4, 5, 6, 7, 8, 9}\n"
     ]
    }
   ],
   "source": [
    "# 3.d Union of sets C, D and E.\n",
    "three_d = three_setC.union(three_setD, three_setE)\n",
    "print(three_d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "7555430b-c831-4084-8986-90936ceaa430",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1, 2, 3, 4, 5, 6, 7, 8, 9}\n"
     ]
    }
   ],
   "source": [
    "# 3.e Add 9 to the set from 3.d.\n",
    "three_d.add(9)\n",
    "three_e = three_d\n",
    "print(three_e)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "5048f785-411b-45d2-98b5-ef6de3b59d76",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "# 3.f Compare this set to the list in one_a using ==.\n",
    "three_f = three_d == one_a\n",
    "print(three_f)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "e7088375-2ad1-43c5-a22e-4f66ab7faa3f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "They are not equal because three_d is a set and one_a is a list.Python's == operator returns False whenever it compares objects of two different types, even if they contain the same values.Furthermore one_a contains an additional integer of 0. \n"
     ]
    }
   ],
   "source": [
    "# 3.g Explain why they are not the same.\n",
    "three_g = (\n",
    "    \"They are not equal because three_d is a set and one_a is a list.\"\n",
    "    \"Python's == operator returns False whenever it compares objects of two different types, even if they contain the same values.\"\n",
    "    \"Furthermore one_a contains an additional integer of 0. \"\n",
    ")\n",
    "print(three_g)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "ad0850e3-75f8-45ea-9706-e90ba42b83b5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "8\n"
     ]
    }
   ],
   "source": [
    "# Problem 4: Changing variable types\n",
    "\n",
    "# 4.a Create a variable of type int with the value of 8.\n",
    "four_a = int(8)\n",
    "print(four_a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "55748b3f-c3bd-43cf-931b-c2cbf6c2aa0f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[]\n"
     ]
    }
   ],
   "source": [
    "# 4.b Create an empty list.\n",
    "four_b = []\n",
    "print(four_b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "093033ba-7e90-4eba-a553-f5dfa4a6040f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[<class 'int'>]\n"
     ]
    }
   ],
   "source": [
    "# 4.c Using type(), add the type of 4.a to this list.\n",
    "four_b.append(type(four_a))\n",
    "four_c=four_b\n",
    "print(four_c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "dd4d4eac-ed5b-4a53-aa7f-7a8155f340b2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "8.39\n"
     ]
    }
   ],
   "source": [
    "# 4.d Add 0.39 to 4.a (this coerces four_a to a float).\n",
    "four_a = four_a + 0.39\n",
    "four_d=four_a\n",
    "print(four_d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "1baee364-3e0b-494c-b7eb-1b526cde0220",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[<class 'int'>, <class 'float'>]\n"
     ]
    }
   ],
   "source": [
    "# 4.e Append the type of the (now float) variable to the list.\n",
    "four_b.append(type(four_a))\n",
    "four_e=four_b\n",
    "print(four_e)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "1aca59ae-b4d5-473a-8096-e90c339ee4ad",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[<class 'int'>, <class 'float'>, 0]\n"
     ]
    }
   ],
   "source": [
    "# 4.f Exponentiate to the -10 power, round to no decimal places, append to list.\n",
    "four_a = round(four_a ** -10)\n",
    "four_b.append(four_a)\n",
    "four_f=four_b\n",
    "print(four_f)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "04f6235e-a1fb-4946-8f2b-0fd4f050281f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[<class 'int'>, <class 'float'>, 0, <class 'int'>]\n"
     ]
    }
   ],
   "source": [
    "# 4.g Append the type to the list.\n",
    "four_b.append(type(four_a))\n",
    "four_g=four_b\n",
    "print(four_g)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "ee3652b5-37d7-4971-80a6-9f1034833314",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{0: <class 'int'>, 1: <class 'float'>, 2: 0, 3: <class 'int'>}\n"
     ]
    }
   ],
   "source": [
    "# Problem 5: More variable type changes (continues from Problem 4)\n",
    "\n",
    "# 5.a Manually create a dictionary where the values are the items in four_b, and the keys are their index in the list. Print the dictionary.\n",
    "five_a = {\n",
    "    0: four_b[0],\n",
    "    1: four_b[1],\n",
    "    2: four_b[2],\n",
    "    3: four_b[3]\n",
    "}\n",
    "print(five_a)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "c5879199-ad20-45b0-b970-f586a83f8025",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "300\n"
     ]
    }
   ],
   "source": [
    "# 5.b Add 300 and coerce it into a string.\n",
    "four_a = str(four_a + 300)\n",
    "five_b=four_a\n",
    "print(five_b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "5385b670-c0c6-48fd-9480-41c5f43a3d7e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[<class 'int'>, <class 'float'>, 0, <class 'int'>, <class 'str'>]\n"
     ]
    }
   ],
   "source": [
    "# 5.c Append the type to the list.\n",
    "four_b.append(type(four_a))\n",
    "five_c= four_b\n",
    "print(five_c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "a37bd250-fdf8-4ed5-90b7-ab90357ac915",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30\n"
     ]
    }
   ],
   "source": [
    "# 5.d Slice the string up to the 2nd element.\n",
    "four_a = four_a[:2]\n",
    "five_d=four_a\n",
    "print(five_d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "42649e61-3a06-4eab-a50b-76354cc329a0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[<class 'int'>, <class 'float'>, 0, <class 'int'>, <class 'str'>, <class 'str'>]\n"
     ]
    }
   ],
   "source": [
    "# 5.e Append the type to the list.\n",
    "four_b.append(type(four_a))\n",
    "five_e=four_b\n",
    "print(five_e)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "9c00ae96-7114-4ed9-9373-e7e34a0a64d5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[3, 0]\n"
     ]
    }
   ],
   "source": [
    "# 5.f Use list comprehension to convert this into a new list of integers.\n",
    "four_a = [int(character) for character in four_a]\n",
    "five_f=four_a\n",
    "print(five_f)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "f218a93e-dd5e-4f5c-9d4b-d84c2add888b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[<class 'int'>, <class 'float'>, 0, <class 'int'>, <class 'str'>, <class 'str'>, <class 'list'>]\n"
     ]
    }
   ],
   "source": [
    "# 5.g Append the type to the list.\n",
    "four_b.append(type(four_a))\n",
    "five_g= four_b\n",
    "print(five_g)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "a1bb6b28-e07c-4bb8-a6a7-a0daf85b15f2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[<class 'int'>, <class 'float'>, 0, <class 'int'>, <class 'str'>, <class 'str'>, <class 'list'>, <class 'set'>]\n"
     ]
    }
   ],
   "source": [
    "# 5.h Append the type of three_setA to the list.\n",
    "four_b.append(type(three_setA))\n",
    "five_h= four_b\n",
    "print(five_h)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
