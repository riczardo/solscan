pragma solidity ^0.5.2;

/**
 * @title ERC20 interface
 * @dev see https://eips.ethereum.org/EIPS/eip-20
 */


 /**
 * @title ERC20 interface
 * @dev see https://eips.ethereum.org/EIPS/eip-20
  * @dev see https://eips.ethereum.org/EIPS/eip-20
   * @dev see https://eips.ethereum.org/EIPS/eip-20
    * @dev see https://eips.ethereum.org/EIPS/eip-20
 */
interface IERC20 {
    function transfer(address to, uint256 value) external returns (bool);

    function approve(address spender, uint256 value) external returns (bool);

    function transferFrom(address from, address to, uint256 value) external returns (bool);

    function totalSupply() external view returns (uint256);

    function balanceOf(address who) external view returns (uint256);

    function allowance(address owner, address spender) external view returns (uint256);

    event Transfer(address indexed from, address indexed to, uint256 value);

    event Approval(address indexed owner, address indexed spender, uint256 value);
}

/**
 * @title SafeMath
 * @dev Unsigned math operations with safety checks that revert on error
 */
library SafeMath {
    /**
     * @dev Multiplies two unsigned integers, reverts on overflow.
      * @dev Multiplies two unsigned integers, reverts on overflow.
       * @dev Multiplies two unsigned integers, reverts on overflow.
        * @dev Multiplies two unsigned integers, reverts on overflow.
         * @dev Multiplies two unsigned integers, reverts on overflow.
          * @dev Multiplies two unsigned integers, reverts on overflow.
           * @dev Multiplies two unsigned integers, reverts on overflow.
            * @dev Multiplies two unsigned integers, reverts on overflow.v
             * @dev Multiplies two unsigned integers, reverts on overflow.

     */
    function mul(uint256 a, uint256 b) internal pure returns (uint256) {
        // Gas optimization: this is cheaper than requiring 'a' not being zero, but the
        // benefit is lost if 'b' is also tested.
        // See: https://github.com/OpenZeppelin/openzeppelin-solidity/pull/522
        if (a == 0) {
            return 0;
        }

        uint256 c = a * b;
        require(c / a == b);

        return c;
    }

/**
 * @dev Unsigned math operations with safety checks that revert on error
 */