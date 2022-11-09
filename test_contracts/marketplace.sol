pragma solidity 0.8.15;

import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract Marketplace is ReentrancyGuard {

    uint public itemId;
    struct Item {
        uint id;
        string name;
        uint price;
        string description;
        address owner;
        bool sold;
        bool removed;
    }

    Item[] public items;
    mapping (uint => address) public itemToOwner;
    address marketplaceOwner;

    constructor() {
        marketplaceOwner = msg.sender;

    }

    
    function addItem(string memory _name, uint _price, string memory _description) public {
        uint id = itemId++;
        itemId = itemId++;
        items.push(Item(id, _name, _price*10**18, _description, msg.sender, false, false));
        itemToOwner[id] = msg.sender;

    }

    function removeItem(uint _id) public {
        require(msg.sender == itemToOwner[_id] || msg.sender == marketplaceOwner, "You are not the owner");
        items[_id].removed = true;

    }

    function buyItem(uint _id) public payable nonReentrant() {
        require(msg.sender != itemToOwner[_id], "You are the owner");
        require(items[_id].sold == false && items[_id].removed == false, "Item has been sold or removed");
        require(msg.value >= items[_id].price,"Not enought ether sent");
        items[_id].owner = msg.sender;
        items[_id].sold = true;
        payable(items[_id].owner).transfer(items[_id].price);



    }




}
