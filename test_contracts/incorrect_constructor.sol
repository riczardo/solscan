pragma solidity ^0.4.15;

contract Missing{
    address private owner;

    modifier onlyowner {
        require(msg.sender==owner);
        _;
    }

    // The name of the constructor should be Missing
    // Anyone can call the IamMissing once the contract is deployed
    function IamMissing()
        public 
    {
        owner = msg.sender;
    }

    function withdraw() 
        public 
        onlyowner
    {
       owner.transfer(this.balance);
    }
}
