contract A {
	uint[] testArray; // dynamic size array

	function f(uint usersCount) public {
		// ...
		testArray.length = usersCount;
		// ...
	}

	function g(uint userIndex, uint val) public {
		// ...
		testArray[userIndex] = val;
		// ...
	}
}