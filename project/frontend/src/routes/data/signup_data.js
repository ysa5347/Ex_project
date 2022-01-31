export const birthList = []
birthList.push({value:"0", name:"선택"})
for (var start=1985;start<=2022;start++){
	birthList.push(
		{ value: start, name: start }
	)
}

export const emailList=[
	{value: "0",name:"직접입력"},
	{value: "1", name:"@naver.com"},
	{value: "2",name:"@gmail.com"},
	{value: "3",name:"@daum.net"}
]