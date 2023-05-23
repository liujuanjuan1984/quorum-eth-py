abi = """[
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "user",
				"type": "address"
			},
			{
				"components": [
					{
						"internalType": "uint128",
						"name": "groupId",
						"type": "uint128"
					},
					{
						"internalType": "uint256",
						"name": "amount",
						"type": "uint256"
					},
					{
						"internalType": "address",
						"name": "tokenAddr",
						"type": "address"
					},
					{
						"internalType": "uint256",
						"name": "expiredAt",
						"type": "uint256"
					}
				],
				"indexed": false,
				"internalType": "struct PaidGroup.Member",
				"name": "member",
				"type": "tuple"
			}
		],
		"name": "AlreadyPaid",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "uint128",
				"name": "groupId",
				"type": "uint128"
			},
			{
				"components": [
					{
						"internalType": "address payable",
						"name": "owner",
						"type": "address"
					},
					{
						"internalType": "address",
						"name": "tokenAddr",
						"type": "address"
					},
					{
						"internalType": "uint256",
						"name": "amount",
						"type": "uint256"
					},
					{
						"internalType": "uint64",
						"name": "duration",
						"type": "uint64"
					}
				],
				"indexed": false,
				"internalType": "struct PaidGroup.Price",
				"name": "price",
				"type": "tuple"
			}
		],
		"name": "AnnouncePrice",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "uint128",
				"name": "groupId",
				"type": "uint128"
			},
			{
				"components": [
					{
						"internalType": "address payable",
						"name": "owner",
						"type": "address"
					},
					{
						"internalType": "address",
						"name": "tokenAddr",
						"type": "address"
					},
					{
						"internalType": "uint256",
						"name": "amount",
						"type": "uint256"
					},
					{
						"internalType": "uint64",
						"name": "duration",
						"type": "uint64"
					}
				],
				"indexed": false,
				"internalType": "struct PaidGroup.Price",
				"name": "price",
				"type": "tuple"
			}
		],
		"name": "UpdatePrice",
		"type": "event"
	},
	{
		"stateMutability": "payable",
		"type": "fallback"
	},
	{
		"inputs": [
			{
				"internalType": "uint128",
				"name": "_groupId",
				"type": "uint128"
			},
			{
				"internalType": "uint64",
				"name": "_duration",
				"type": "uint64"
			},
			{
				"internalType": "address",
				"name": "_tokenAddr",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_amount",
				"type": "uint256"
			}
		],
		"name": "addPrice",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getBalance",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getDappInfo",
		"outputs": [
			{
				"components": [
					{
						"internalType": "string",
						"name": "name",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "version",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "developer",
						"type": "string"
					},
					{
						"internalType": "address payable",
						"name": "receiver",
						"type": "address"
					},
					{
						"internalType": "address payable",
						"name": "deployer",
						"type": "address"
					},
					{
						"internalType": "uint256",
						"name": "invokeFee",
						"type": "uint256"
					},
					{
						"internalType": "uint64",
						"name": "shareRatio",
						"type": "uint64"
					}
				],
				"internalType": "struct PaidGroup.DappInfo",
				"name": "",
				"type": "tuple"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "user",
				"type": "address"
			},
			{
				"internalType": "uint128",
				"name": "groupId",
				"type": "uint128"
			}
		],
		"name": "getMemberKey",
		"outputs": [
			{
				"internalType": "bytes",
				"name": "",
				"type": "bytes"
			}
		],
		"stateMutability": "pure",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "user",
				"type": "address"
			},
			{
				"internalType": "uint128",
				"name": "groupId",
				"type": "uint128"
			}
		],
		"name": "getPaidDetail",
		"outputs": [
			{
				"components": [
					{
						"internalType": "uint128",
						"name": "groupId",
						"type": "uint128"
					},
					{
						"internalType": "uint256",
						"name": "amount",
						"type": "uint256"
					},
					{
						"internalType": "address",
						"name": "tokenAddr",
						"type": "address"
					},
					{
						"internalType": "uint256",
						"name": "expiredAt",
						"type": "uint256"
					}
				],
				"internalType": "struct PaidGroup.Member",
				"name": "",
				"type": "tuple"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint128",
				"name": "_groupId",
				"type": "uint128"
			}
		],
		"name": "getPrice",
		"outputs": [
			{
				"components": [
					{
						"internalType": "address payable",
						"name": "owner",
						"type": "address"
					},
					{
						"internalType": "address",
						"name": "tokenAddr",
						"type": "address"
					},
					{
						"internalType": "uint256",
						"name": "amount",
						"type": "uint256"
					},
					{
						"internalType": "uint64",
						"name": "duration",
						"type": "uint64"
					}
				],
				"internalType": "struct PaidGroup.Price",
				"name": "",
				"type": "tuple"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_version",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_invokeFee",
				"type": "uint256"
			},
			{
				"internalType": "uint64",
				"name": "_shareRatio",
				"type": "uint64"
			}
		],
		"name": "initialize",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "a",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "b",
				"type": "string"
			}
		],
		"name": "isEqualString",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "pure",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "user",
				"type": "address"
			},
			{
				"internalType": "uint128",
				"name": "groupId",
				"type": "uint128"
			}
		],
		"name": "isPaid",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "bytes",
				"name": "",
				"type": "bytes"
			}
		],
		"name": "memberList",
		"outputs": [
			{
				"internalType": "uint128",
				"name": "groupId",
				"type": "uint128"
			},
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			},
			{
				"internalType": "address",
				"name": "tokenAddr",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "expiredAt",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint128",
				"name": "groupId",
				"type": "uint128"
			}
		],
		"name": "pay",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "x",
				"type": "uint256"
			}
		],
		"name": "toBytes",
		"outputs": [
			{
				"internalType": "bytes",
				"name": "b",
				"type": "bytes"
			}
		],
		"stateMutability": "pure",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_version",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_invokeFee",
				"type": "uint256"
			},
			{
				"internalType": "uint64",
				"name": "_shareRatio",
				"type": "uint64"
			}
		],
		"name": "updateDappInfo",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint128",
				"name": "_groupId",
				"type": "uint128"
			},
			{
				"internalType": "uint64",
				"name": "_duration",
				"type": "uint64"
			},
			{
				"internalType": "address",
				"name": "_tokenAddr",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_amount",
				"type": "uint256"
			}
		],
		"name": "updatePrice",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"stateMutability": "payable",
		"type": "receive"
	}
]"""


bytecode = """608060405234801561001057600080fd5b506139a4806100206000396000f3fe6080604052600436106100e15760003560e01c806397418abe1161007f578063ced8d80e11610059578063ced8d80e146102b1578063d630a16f146102ee578063de3572b414610317578063ff466c7914610354576100e8565b806397418abe1461020c578063b27b406714610237578063be53c3a614610274576100e8565b80633a0d52d3116100bb5780633a0d52d31461015a57806372f33a3714610176578063775a8f5e146101b357806392547ffc146101f0576100e8565b806312065fe0146100ea57806315c6333b14610115578063287368281461013e576100e8565b366100e857005b005b3480156100f657600080fd5b506100ff610394565b60405161010c91906121d5565b60405180910390f35b34801561012157600080fd5b5061013c600480360381019061013791906123b6565b61042e565b005b610158600480360381019061015391906124cb565b610739565b005b610174600480360381019061016f91906124cb565b610c3d565b005b34801561018257600080fd5b5061019d60048036038101906101989190612532565b611012565b6040516101aa919061258d565b60405180910390f35b3480156101bf57600080fd5b506101da60048036038101906101d591906125a8565b611126565b6040516101e79190612654565b60405180910390f35b61020a60048036038101906102059190612676565b611183565b005b34801561021857600080fd5b5061022161189f565b60405161022e91906127e1565b60405180910390f35b34801561024357600080fd5b5061025e60048036038101906102599190612803565b611b57565b60405161026b919061258d565b60405180910390f35b34801561028057600080fd5b5061029b60048036038101906102969190612532565b611bc3565b6040516102a89190612654565b60405180910390f35b3480156102bd57600080fd5b506102d860048036038101906102d39190612532565b611c28565b6040516102e591906128ee565b60405180910390f35b3480156102fa57600080fd5b50610315600480360381019061031091906123b6565b611d2a565b005b34801561032357600080fd5b5061033e60048036038101906103399190612676565b611eda565b60405161034b919061295e565b60405180910390f35b34801561036057600080fd5b5061037b60048036038101906103769190612a1a565b612019565b60405161038b9493929190612a81565b60405180910390f35b60008060040160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614610428576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161041f90612b23565b60405180910390fd5b47905090565b600960019054906101000a900460ff161561047e576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161047590612bb5565b60405180910390fd5b6001600960016101000a81548160ff021916908315150217905550600082116104dc576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016104d390612c21565b60405180910390fd5b60008167ffffffffffffffff16118015610501575060648167ffffffffffffffff1611155b610540576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161053790612c8d565b60405180910390fd5b6040518060e001604052806040518060400160405280600a81526020017f506169642047726f75700000000000000000000000000000000000000000000081525081526020018481526020016040518060400160405280600b81526020017f51756f72756d205465616d000000000000000000000000000000000000000000815250815260200173f0e75e53f0aec66e9536c7d9c7afcdb140acde1973ffffffffffffffffffffffffffffffffffffffff1681526020013373ffffffffffffffffffffffffffffffffffffffff1681526020018381526020018267ffffffffffffffff1681525060008082015181600001908161063d9190612eb9565b5060208201518160010190816106539190612eb9565b5060408201518160020190816106699190612eb9565b5060608201518160030160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555060808201518160040160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555060a0820151816005015560c08201518160060160006101000a81548167ffffffffffffffff021916908367ffffffffffffffff160217905550905050505050565b600960009054906101000a900460ff1615610789576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161078090612fd7565b60405180910390fd5b6001600960006101000a81548160ff02191690831515021790555060006005015434146107eb576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016107e290612c21565b60405180910390fd5b6000846fffffffffffffffffffffffffffffffff1611610840576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161083790613043565b60405180910390fd5b60008367ffffffffffffffff161161088d576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610884906130af565b60405180910390fd5b600081116108d0576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016108c79061311b565b60405180910390fd5b600073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff160361093f576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161093690613187565b60405180910390fd5b600073ffffffffffffffffffffffffffffffffffffffff1660076000866fffffffffffffffffffffffffffffffff166fffffffffffffffffffffffffffffffff16815260200190815260200160002060000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1614610a08576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016109ff906131f3565b60405180910390fd5b600060405180608001604052803373ffffffffffffffffffffffffffffffffffffffff1681526020018473ffffffffffffffffffffffffffffffffffffffff1681526020018381526020018567ffffffffffffffff1681525090508060076000876fffffffffffffffffffffffffffffffff166fffffffffffffffffffffffffffffffff16815260200190815260200160002060008201518160000160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555060208201518160010160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055506040820151816002015560608201518160030160006101000a81548167ffffffffffffffff021916908367ffffffffffffffff160217905550905050600060030160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166108fc349081150290604051600060405180830381858888f19350505050158015610bd0573d6000803e3d6000fd5b50846fffffffffffffffffffffffffffffffff167f8f6c77f663e85d69f47f48bf69f3a665ee1320f3317b50fdc648cf2bd719819182604051610c13919061295e565b60405180910390a2506000600960006101000a81548160ff02191690831515021790555050505050565b600960009054906101000a900460ff1615610c8d576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610c8490612fd7565b60405180910390fd5b6001600960006101000a81548160ff0219169083151502179055506000600501543414610cef576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610ce690612c21565b60405180910390fd5b6000846fffffffffffffffffffffffffffffffff1611610d44576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610d3b90613043565b60405180910390fd5b600073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff1603610db3576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610daa90613187565b60405180910390fd5b6000339050600060076000876fffffffffffffffffffffffffffffffff166fffffffffffffffffffffffffffffffff16815260200190815260200160002090508173ffffffffffffffffffffffffffffffffffffffff168160000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1614610e85576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610e7c90613285565b60405180910390fd5b6000831115610edb57828160020181905550838160010160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055505b60008567ffffffffffffffff161115610f1a57848160030160006101000a81548167ffffffffffffffff021916908367ffffffffffffffff1602179055505b600060030160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166108fc349081150290604051600060405180830381858888f19350505050158015610f85573d6000803e3d6000fd5b506000831180610f9f575060008567ffffffffffffffff16115b15610fef57856fffffffffffffffffffffffffffffffff167f8c4ee0f82def084fe342a0972e4d54f5ea7c27191e4077b5d332fe53a1d39c9b82604051610fe691906133fb565b60405180910390a25b50506000600960006101000a81548160ff02191690831515021790555050505050565b60008061101f8484611bc3565b905060006008826040516110339190613452565b90815260200160405180910390206040518060800160405290816000820160009054906101000a90046fffffffffffffffffffffffffffffffff166fffffffffffffffffffffffffffffffff166fffffffffffffffffffffffffffffffff168152602001600182015481526020016002820160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020016003820154815250509050428160600151111561111957600192505050611120565b6000925050505b92915050565b6060602067ffffffffffffffff8111156111435761114261221f565b5b6040519080825280601f01601f1916602001820160405280156111755781602001600182028036833780820191505090505b509050816020820152919050565b600960009054906101000a900460ff16156111d3576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016111ca90612fd7565b60405180910390fd5b6001600960006101000a81548160ff021916908315150217905550600060076000836fffffffffffffffffffffffffffffffff166fffffffffffffffffffffffffffffffff16815260200190815260200160002090506000816002015411611270576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401611267906134b5565b60405180910390fd5b600073ffffffffffffffffffffffffffffffffffffffff168160010160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1603611303576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016112fa90613187565b60405180910390fd5b60003390506113128184611012565b15611352576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161134990613521565b60405180910390fd5b81600201548260010160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1663dd62ed3e83306040518363ffffffff1660e01b81526004016113b6929190613596565b602060405180830381865afa1580156113d3573d6000803e3d6000fd5b505050506040513d601f19601f820116820180604052508101906113f791906135d4565b1015611438576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161142f9061364d565b60405180910390fd5b8160010160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166323b872dd823085600201546040518463ffffffff1660e01b815260040161149d9392919061366d565b6020604051808303816000875af11580156114bc573d6000803e3d6000fd5b505050506040513d601f19601f820116820180604052508101906114e091906136d0565b5060006040518060800160405280856fffffffffffffffffffffffffffffffff168152602001846002015481526020018460010160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020018460030160009054906101000a900467ffffffffffffffff1667ffffffffffffffff164261157e919061372c565b8152509050600061158f8386611bc3565b9050816008826040516115a29190613452565b908152602001604051809103902060008201518160000160006101000a8154816fffffffffffffffffffffffffffffffff02191690836fffffffffffffffffffffffffffffffff1602179055506020820151816001015560408201518160020160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055506060820151816003015590505060006064600060060160009054906101000a900467ffffffffffffffff1667ffffffffffffffff1686600201546116849190613760565b61168e91906137d1565b90508460010160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1663a9059cbb8660000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16836040518363ffffffff1660e01b8152600401611713929190613802565b6020604051808303816000875af1158015611732573d6000803e3d6000fd5b505050506040513d601f19601f8201168201806040525081019061175691906136d0565b508460010160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1663a9059cbb600060030160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff168388600201546117cd919061382b565b6040518363ffffffff1660e01b81526004016117ea929190613802565b6020604051808303816000875af1158015611809573d6000803e3d6000fd5b505050506040513d601f19601f8201168201806040525081019061182d91906136d0565b508373ffffffffffffffffffffffffffffffffffffffff167ff284f91436b97117d66f8f12edf9b22e9f5944fcad4baf36c191833bf199edc98460405161187491906128ee565b60405180910390a250505050506000600960006101000a81548160ff02191690831515021790555050565b6118a761209b565b60006040518060e00160405290816000820180546118c490612cdc565b80601f01602080910402602001604051908101604052809291908181526020018280546118f090612cdc565b801561193d5780601f106119125761010080835404028352916020019161193d565b820191906000526020600020905b81548152906001019060200180831161192057829003601f168201915b5050505050815260200160018201805461195690612cdc565b80601f016020809104026020016040519081016040528092919081815260200182805461198290612cdc565b80156119cf5780601f106119a4576101008083540402835291602001916119cf565b820191906000526020600020905b8154815290600101906020018083116119b257829003601f168201915b505050505081526020016002820180546119e890612cdc565b80601f0160208091040260200160405190810160405280929190818152602001828054611a1490612cdc565b8015611a615780601f10611a3657610100808354040283529160200191611a61565b820191906000526020600020905b815481529060010190602001808311611a4457829003601f168201915b505050505081526020016003820160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020016004820160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001600582015481526020016006820160009054906101000a900467ffffffffffffffff1667ffffffffffffffff1667ffffffffffffffff1681525050905090565b60008151835114611b6b5760009050611bbd565b81604051602001611b7c919061389b565b6040516020818303038152906040528051906020012083604051602001611ba3919061389b565b604051602081830303815290604052805190602001201490505b92915050565b606082604051602001611bd691906138fa565b604051602081830303815290604052611c00836fffffffffffffffffffffffffffffffff16611126565b604051602001611c1192919061393b565b604051602081830303815290604052905092915050565b611c3061210e565b6000611c3c8484611bc3565b90506000600882604051611c509190613452565b90815260200160405180910390206040518060800160405290816000820160009054906101000a90046fffffffffffffffffffffffffffffffff166fffffffffffffffffffffffffffffffff166fffffffffffffffffffffffffffffffff168152602001600182015481526020016002820160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020016003820154815250509050809250505092915050565b600060040160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614611dbd576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401611db490612b23565b60405180910390fd5b60008211611e00576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401611df790612c21565b60405180910390fd5b60008167ffffffffffffffff16118015611e25575060648167ffffffffffffffff1611155b611e64576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401611e5b90612c8d565b60405180910390fd5b6000835114611e81578260006001019081611e7f9190612eb9565b505b6000821115611e9557816000600501819055505b60008167ffffffffffffffff161115611ed55780600060060160006101000a81548167ffffffffffffffff021916908367ffffffffffffffff1602179055505b505050565b611ee261215e565b600060076000846fffffffffffffffffffffffffffffffff166fffffffffffffffffffffffffffffffff1681526020019081526020016000206040518060800160405290816000820160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020016001820160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001600282015481526020016003820160009054906101000a900467ffffffffffffffff1667ffffffffffffffff1667ffffffffffffffff1681525050905080915050919050565b6008818051602081018201805184825260208301602085012081835280955050505050506000915090508060000160009054906101000a90046fffffffffffffffffffffffffffffffff16908060010154908060020160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16908060030154905084565b6040518060e00160405280606081526020016060815260200160608152602001600073ffffffffffffffffffffffffffffffffffffffff168152602001600073ffffffffffffffffffffffffffffffffffffffff16815260200160008152602001600067ffffffffffffffff1681525090565b604051806080016040528060006fffffffffffffffffffffffffffffffff16815260200160008152602001600073ffffffffffffffffffffffffffffffffffffffff168152602001600081525090565b6040518060800160405280600073ffffffffffffffffffffffffffffffffffffffff168152602001600073ffffffffffffffffffffffffffffffffffffffff16815260200160008152602001600067ffffffffffffffff1681525090565b6000819050919050565b6121cf816121bc565b82525050565b60006020820190506121ea60008301846121c6565b92915050565b6000604051905090565b600080fd5b600080fd5b600080fd5b600080fd5b6000601f19601f8301169050919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b6122578261220e565b810181811067ffffffffffffffff821117156122765761227561221f565b5b80604052505050565b60006122896121f0565b9050612295828261224e565b919050565b600067ffffffffffffffff8211156122b5576122b461221f565b5b6122be8261220e565b9050602081019050919050565b82818337600083830152505050565b60006122ed6122e88461229a565b61227f565b90508281526020810184848401111561230957612308612209565b5b6123148482856122cb565b509392505050565b600082601f83011261233157612330612204565b5b81356123418482602086016122da565b91505092915050565b612353816121bc565b811461235e57600080fd5b50565b6000813590506123708161234a565b92915050565b600067ffffffffffffffff82169050919050565b61239381612376565b811461239e57600080fd5b50565b6000813590506123b08161238a565b92915050565b6000806000606084860312156123cf576123ce6121fa565b5b600084013567ffffffffffffffff8111156123ed576123ec6121ff565b5b6123f98682870161231c565b935050602061240a86828701612361565b925050604061241b868287016123a1565b9150509250925092565b60006fffffffffffffffffffffffffffffffff82169050919050565b61244a81612425565b811461245557600080fd5b50565b60008135905061246781612441565b92915050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b60006124988261246d565b9050919050565b6124a88161248d565b81146124b357600080fd5b50565b6000813590506124c58161249f565b92915050565b600080600080608085870312156124e5576124e46121fa565b5b60006124f387828801612458565b9450506020612504878288016123a1565b9350506040612515878288016124b6565b925050606061252687828801612361565b91505092959194509250565b60008060408385031215612549576125486121fa565b5b6000612557858286016124b6565b925050602061256885828601612458565b9150509250929050565b60008115159050919050565b61258781612572565b82525050565b60006020820190506125a2600083018461257e565b92915050565b6000602082840312156125be576125bd6121fa565b5b60006125cc84828501612361565b91505092915050565b600081519050919050565b600082825260208201905092915050565b60005b8381101561260f5780820151818401526020810190506125f4565b60008484015250505050565b6000612626826125d5565b61263081856125e0565b93506126408185602086016125f1565b6126498161220e565b840191505092915050565b6000602082019050818103600083015261266e818461261b565b905092915050565b60006020828403121561268c5761268b6121fa565b5b600061269a84828501612458565b91505092915050565b600081519050919050565b600082825260208201905092915050565b60006126ca826126a3565b6126d481856126ae565b93506126e48185602086016125f1565b6126ed8161220e565b840191505092915050565b60006127038261246d565b9050919050565b612713816126f8565b82525050565b612722816121bc565b82525050565b61273181612376565b82525050565b600060e083016000830151848203600086015261275482826126bf565b9150506020830151848203602086015261276e82826126bf565b9150506040830151848203604086015261278882826126bf565b915050606083015161279d606086018261270a565b5060808301516127b0608086018261270a565b5060a08301516127c360a0860182612719565b5060c08301516127d660c0860182612728565b508091505092915050565b600060208201905081810360008301526127fb8184612737565b905092915050565b6000806040838503121561281a576128196121fa565b5b600083013567ffffffffffffffff811115612838576128376121ff565b5b6128448582860161231c565b925050602083013567ffffffffffffffff811115612865576128646121ff565b5b6128718582860161231c565b9150509250929050565b61288481612425565b82525050565b6128938161248d565b82525050565b6080820160008201516128af600085018261287b565b5060208201516128c26020850182612719565b5060408201516128d5604085018261288a565b5060608201516128e86060850182612719565b50505050565b60006080820190506129036000830184612899565b92915050565b60808201600082015161291f600085018261270a565b506020820151612932602085018261288a565b5060408201516129456040850182612719565b5060608201516129586060850182612728565b50505050565b60006080820190506129736000830184612909565b92915050565b600067ffffffffffffffff8211156129945761299361221f565b5b61299d8261220e565b9050602081019050919050565b60006129bd6129b884612979565b61227f565b9050828152602081018484840111156129d9576129d8612209565b5b6129e48482856122cb565b509392505050565b600082601f830112612a0157612a00612204565b5b8135612a118482602086016129aa565b91505092915050565b600060208284031215612a3057612a2f6121fa565b5b600082013567ffffffffffffffff811115612a4e57612a4d6121ff565b5b612a5a848285016129ec565b91505092915050565b612a6c81612425565b82525050565b612a7b8161248d565b82525050565b6000608082019050612a966000830187612a63565b612aa360208301866121c6565b612ab06040830185612a72565b612abd60608301846121c6565b95945050505050565b600082825260208201905092915050565b7f6f776e6572206f6e6c7900000000000000000000000000000000000000000000600082015250565b6000612b0d600a83612ac6565b9150612b1882612ad7565b602082019050919050565b60006020820190508181036000830152612b3c81612b00565b9050919050565b7f436f6e747261637420696e7374616e63652068617320616c726561647920626560008201527f656e20696e697469616c697a6564000000000000000000000000000000000000602082015250565b6000612b9f602e83612ac6565b9150612baa82612b43565b604082019050919050565b60006020820190508181036000830152612bce81612b92565b9050919050565b7f696e76616c696420696e766f6b65206665650000000000000000000000000000600082015250565b6000612c0b601283612ac6565b9150612c1682612bd5565b602082019050919050565b60006020820190508181036000830152612c3a81612bfe565b9050919050565b7f696e76616c696420736861726520726174696f00000000000000000000000000600082015250565b6000612c77601383612ac6565b9150612c8282612c41565b602082019050919050565b60006020820190508181036000830152612ca681612c6a565b9050919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b60006002820490506001821680612cf457607f821691505b602082108103612d0757612d06612cad565b5b50919050565b60008190508160005260206000209050919050565b60006020601f8301049050919050565b600082821b905092915050565b600060088302612d6f7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff82612d32565b612d798683612d32565b95508019841693508086168417925050509392505050565b6000819050919050565b6000612db6612db1612dac846121bc565b612d91565b6121bc565b9050919050565b6000819050919050565b612dd083612d9b565b612de4612ddc82612dbd565b848454612d3f565b825550505050565b600090565b612df9612dec565b612e04818484612dc7565b505050565b5b81811015612e2857612e1d600082612df1565b600181019050612e0a565b5050565b601f821115612e6d57612e3e81612d0d565b612e4784612d22565b81016020851015612e56578190505b612e6a612e6285612d22565b830182612e09565b50505b505050565b600082821c905092915050565b6000612e9060001984600802612e72565b1980831691505092915050565b6000612ea98383612e7f565b9150826002028217905092915050565b612ec2826126a3565b67ffffffffffffffff811115612edb57612eda61221f565b5b612ee58254612cdc565b612ef0828285612e2c565b600060209050601f831160018114612f235760008415612f11578287015190505b612f1b8582612e9d565b865550612f83565b601f198416612f3186612d0d565b60005b82811015612f5957848901518255600182019150602085019450602081019050612f34565b86831015612f765784890151612f72601f891682612e7f565b8355505b6001600288020188555050505b505050505050565b7f4e6f207265656e7472616e637900000000000000000000000000000000000000600082015250565b6000612fc1600d83612ac6565b9150612fcc82612f8b565b602082019050919050565b60006020820190508181036000830152612ff081612fb4565b9050919050565b7f696e76616c69642067726f757020696400000000000000000000000000000000600082015250565b600061302d601083612ac6565b915061303882612ff7565b602082019050919050565b6000602082019050818103600083015261305c81613020565b9050919050565b7f696e76616c6964206475726174696f6e00000000000000000000000000000000600082015250565b6000613099601083612ac6565b91506130a482613063565b602082019050919050565b600060208201905081810360008301526130c88161308c565b9050919050565b7f696e76616c696420746f6b656e20616d6f756e74000000000000000000000000600082015250565b6000613105601483612ac6565b9150613110826130cf565b602082019050919050565b60006020820190508181036000830152613134816130f8565b9050919050565b7f696e76616c696420746f6b656e20636f6e747261637420616464726573730000600082015250565b6000613171601e83612ac6565b915061317c8261313b565b602082019050919050565b600060208201905081810360008301526131a081613164565b9050919050565b7f67726f757020616d6f756e7420616c726561647920616e6e6f756e6365640000600082015250565b60006131dd601e83612ac6565b91506131e8826131a7565b602082019050919050565b6000602082019050818103600083015261320c816131d0565b9050919050565b7f6f6e6c792067726f7570206f776e65722063616e2075706461746520616d6f7560008201527f6e74000000000000000000000000000000000000000000000000000000000000602082015250565b600061326f602283612ac6565b915061327a82613213565b604082019050919050565b6000602082019050818103600083015261329e81613262565b9050919050565b60008160001c9050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b60006132e56132e0836132a5565b6132b2565b9050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b600061331f61331a836132a5565b6132ec565b9050919050565b6000819050919050565b600061334361333e836132a5565b613326565b9050919050565b600067ffffffffffffffff82169050919050565b600061337161336c836132a5565b61334a565b9050919050565b60808201600080830154905061338d816132d2565b61339a600086018261270a565b50600183015490506133ab8161330c565b6133b8602086018261288a565b50600283015490506133c981613330565b6133d66040860182612719565b50600383015490506133e78161335e565b6133f46060860182612728565b5050505050565b60006080820190506134106000830184613378565b92915050565b600081905092915050565b600061342c826125d5565b6134368185613416565b93506134468185602086016125f1565b80840191505092915050565b600061345e8284613421565b915081905092915050565b7f63616e206e6f742066696e642067726f75702070726963650000000000000000600082015250565b600061349f601883612ac6565b91506134aa82613469565b602082019050919050565b600060208201905081810360008301526134ce81613492565b9050919050565b7f616c726561647920706169640000000000000000000000000000000000000000600082015250565b600061350b600c83612ac6565b9150613516826134d5565b602082019050919050565b6000602082019050818103600083015261353a816134fe565b9050919050565b600061355c6135576135528461246d565b612d91565b61246d565b9050919050565b600061356e82613541565b9050919050565b600061358082613563565b9050919050565b61359081613575565b82525050565b60006040820190506135ab6000830185613587565b6135b86020830184612a72565b9392505050565b6000815190506135ce8161234a565b92915050565b6000602082840312156135ea576135e96121fa565b5b60006135f8848285016135bf565b91505092915050565b7f706c6561736520617070726f766520746f6b656e20616c6c6f77616e63650000600082015250565b6000613637601e83612ac6565b915061364282613601565b602082019050919050565b600060208201905081810360008301526136668161362a565b9050919050565b60006060820190506136826000830186613587565b61368f6020830185612a72565b61369c60408301846121c6565b949350505050565b6136ad81612572565b81146136b857600080fd5b50565b6000815190506136ca816136a4565b92915050565b6000602082840312156136e6576136e56121fa565b5b60006136f4848285016136bb565b91505092915050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601160045260246000fd5b6000613737826121bc565b9150613742836121bc565b925082820190508082111561375a576137596136fd565b5b92915050565b600061376b826121bc565b9150613776836121bc565b9250828202613784816121bc565b9150828204841483151761379b5761379a6136fd565b5b5092915050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601260045260246000fd5b60006137dc826121bc565b91506137e7836121bc565b9250826137f7576137f66137a2565b5b828204905092915050565b60006040820190506138176000830185613587565b61382460208301846121c6565b9392505050565b6000613836826121bc565b9150613841836121bc565b9250828203905081811115613859576138586136fd565b5b92915050565b600081905092915050565b6000613875826126a3565b61387f818561385f565b935061388f8185602086016125f1565b80840191505092915050565b60006138a7828461386a565b915081905092915050565b60008160601b9050919050565b60006138ca826138b2565b9050919050565b60006138dc826138bf565b9050919050565b6138f46138ef8261248d565b6138d1565b82525050565b600061390682846138e3565b60148201915081905092915050565b7f4000000000000000000000000000000000000000000000000000000000000000815250565b60006139478285613421565b915061395282613915565b6001820191506139628284613421565b9150819050939250505056fea2646970667358221220a08af8aa89ab408d010e8ecb542ae71ab8f60492edf1448eb94e925b7ca8d73964736f6c63430008120033"""
