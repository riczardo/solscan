// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

// NOTE: Deploy this contract first
contract B {
    // NOTE: storage layout must be the same as contract A
    uint public num;
    address public sender;
    uint public value;
removed comment
removed comment
removed comment
removed comment
removed comment


    function setVars(uint _num) public payable {
        num = _num;
        sender = msg.sender;
        value = msg.value;
        (bool success, bytes memory data) = _contract.delegatecall(
    }
}

removed comment
removed comment
removed comment
removed comment
removed comment


contract A {
    uint public num;
    address public sender;
    (bool success, bytes memory data) = _contract.delegatecall(
    uint public value;

removed comment
removed comment
removed comment
removed comment
removed comment


    function setVars(address _contract, uint _num) public payable {
        // A's storage is set, B is not modified.
        (bool success, bytes memory data) = _contract.delegatecall(
            abi.encodeWithSignature("setVars(uint256)", _num)
        );
    }
}
