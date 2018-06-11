pragma solidity ^0.4.15;

contract impulse_001
{

	string public symbol;
    string public  name;
    uint8 public decimals;
    uint public _totalSupply;

    mapping(address => uint) balances;
    mapping(address => mapping(address => uint)) allowed;

    // ---------------------------------------------------------------------------------------------
    // Constructor
    // ---------------------------------------------------------------------------------------------
    function impulse_001() public {
        symbol = "IMPL";
        name = "IMPULSE_v0.0.1";
        decimals = 18;
        _totalSupply = 1000000 * 10**uint(decimals);
        balances[owner] = _totalSupply;
        Transfer(address(0), owner, _totalSupply);
    }

	// ---------------------------------------------------------------------------------------------
	// Total Supply 
	// ---------------------------------------------------------------------------------------------
	function totalSupply() public constant returns (uint) {
        return _totalSupply  - balances[address(0)];
    }

    // ---------------------------------------------------------------------------------------------
    // Getting balance of an address
    // ---------------------------------------------------------------------------------------------
    function balanceOf(address tokenOwner) public constant returns (uint balance) {
        return balances[tokenOwner];
    }

    // ---------------------------------------------------------------------------------------------
    // Returns the amount of tokens approved by the owner 
    // that can be transferred to the spenders account
    // ---------------------------------------------------------------------------------------------
    function allowance(address tokenOwner,address spender) 
    public constant returns (uint remaining) {
        return allowed[tokenOwner][spender];
    }

    // ---------------------------------------------------------------------------------------------
    // Transfer tokens from owners account to the "to" account
    // - Owner must have sufficient balance to transfer tokens
    // - 0 value transfers are allowed
    // ---------------------------------------------------------------------------------------------
    function transfer(address to, uint tokens) public returns (bool success) {
        balances[msg.sender] = balances[msg.sender].sub(tokens);
        balances[to] = balances[to].add(tokens);
        Transfer(msg.sender, to, tokens);
        return true;
    }

    // ---------------------------------------------------------------------------------------------
    // Token owner can approve for "spender" to transferFrom() tokens from the owners account
    //
    // https://github.com/ethereum/EIPs/blob/master/EIPS/eip-20-token-standard.md
    // recommends that there are no checks for the approval double-spend attack
    // as this should be implemented in user interfaces  
    // ---------------------------------------------------------------------------------------------
    function approve(address spender, uint tokens) public returns (bool success) {
        allowed[msg.sender][spender] = tokens;
        Approval(msg.sender, spender, tokens);
        return true;
    } 

    // ---------------------------------------------------------------------------------------------
    // Transfer tokens from the "from" account to the "to" account
    // The calling account must have sufficient tokens approved for spending from the "from" account
    // The "from" account must have sufficient balance to transfer
    // Spender must have sufficient allowance to transfer
    // 0 value transfers are allowed
    // ---------------------------------------------------------------------------------------------
    function transferFrom(address from, address to, uint tokens) public returns (bool success) {
        balances[from] = balances[from].sub(tokens);
        allowed[from][msg.sender] = allowed[from][msg.sender].sub(tokens);
        balances[to] = balances[to].add(tokens);
        Transfer(from, to, tokens);
        return true;
    }

    // ---------------------------------------------------------------------------------------------
    // Token owner can approve for "Spender" to transferFrom "tokens" from the token owner's account
    // The "spender" contract function receiveApproval() is then executed
  	//----------------------------------------------------------------------------------------------
  	function approveAndCall(address spender, uint tokens, bytes data) 
  	public returns (bool success) {
        allowed[msg.sender][spender] = tokens;
        Approval(msg.sender, spender, tokens);
        ApproveAndCallFallBack(spender).receiveApproval(msg.sender, tokens, this, data);
        return true;
    }

    // ---------------------------------------------------------------------------------------------
    // Owner can transfer out any accidentally sent ERC20 tokens
    // ---------------------------------------------------------------------------------------------
    function transferAnyERC20Token(address tokenAddress, uint tokens) 
    public onlyOwner returns (bool success) {
        return ERC20Interface(tokenAddress).transfer(owner, tokens);
    }

    // ---------------------------------------------------------------------------------------------
    // Don't accept ETH
    // ---------------------------------------------------------------------------------------------
    function () public payable {
        revert();
    }

}


// -------------------------------------------------------------------------------------------------
// ERC Token Standard #20 Interface
// -------------------------------------------------------------------------------------------------
contract ERC20Interface {
    function totalSupply() public constant returns (uint);
    function balanceOf(address tokenOwner) public constant returns (uint balance);
    function allowance(address tokenOwner,address spender) public constant returns (uint remaining);
    function transfer(address to, uint tokens) public returns (bool success);
    function approve(address spender, uint tokens) public returns (bool success);
    function transferFrom(address from, address to, uint tokens) public returns (bool success);

    event Transfer(address indexed from, address indexed to, uint tokens);
    event Approval(address indexed tokenOwner, address indexed spender, uint tokens);
}


// -------------------------------------------------------------------------------------------------
// Owned contract
// -------------------------------------------------------------------------------------------------
contract Owned {
    address public owner;
    address public newOwner;

    event OwnershipTransferred(address indexed _from, address indexed _to);

    function Owned() public {
        owner = msg.sender;
    }

    modifier onlyOwner {
        require(msg.sender == owner);
        _;
    }

    function transferOwnership(address _newOwner) public onlyOwner {
        newOwner = _newOwner;
    }
    function acceptOwnership() public {
        require(msg.sender == newOwner);
        OwnershipTransferred(owner, newOwner);
        owner = newOwner;
        newOwner = address(0);
    }
}


// ----------------------------------------------------------------------------
// Contract function to receive approval and execute function in one call
// ----------------------------------------------------------------------------
contract ApproveAndCallFallBack {
    function receiveApproval(address from, uint256 tokens, address token, bytes data) public;
}


// -------------------------------------------------------------------------------------------------
// Safe maths
// -------------------------------------------------------------------------------------------------
library SafeMath {
    function add(uint a, uint b) internal pure returns (uint c) {
        c = a + b;
        require(c >= a);
    }
    function sub(uint a, uint b) internal pure returns (uint c) {
        require(b <= a);
        c = a - b;
    }
    function mul(uint a, uint b) internal pure returns (uint c) {
        c = a * b;
        require(a == 0 || c / a == b);
    }
    function div(uint a, uint b) internal pure returns (uint c) {
        require(b > 0);
        c = a / b;
    }
}