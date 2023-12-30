// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract demo {
  string a;
  function assign(string memory b) public {
    a=b;
  }
  function print() public view returns(string memory){
    return a;
  }

}
