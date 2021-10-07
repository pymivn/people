**[qrrr](https://ctf.snyk.io/challenges#qrrr-82)**

Bài này ban tổ chức đưa cho thí sinh một file ảnh QR đủ màu sắc.
![File QR](https://i.ibb.co/j686m4y/flag.png)
Lấy zalo ra quét thử không được, như vậy file này thực ra không phải QR đúng chuẩn.
Nhìn vào màu sắc của hình thì có vẻ như QR này gồm 3 mã QR tương ứng với 3 đoạn mà khi ghép lại với nhau ta có được flag.
OK. Giờ dùng một công cụ đơn giản để xử lý file ảnh này. Link Tool: [StegOnline (georgeom.net)](https://stegonline.georgeom.net/upload)
Một file ảnh màu RGB này có 3 bit planes là (Red, Green, Blue).
Thử với plane Red với giá trị là 6/8 ta có:
![Try 1!](https://i.ibb.co/zX5y40c/red.png)
Trông có vẻ ổn nhưng với ảnh QR để quét thì ta cần reverse lại. Sau khi reverse ta được
![Reverse Try 1](https://i.ibb.co/x5ppDF5/download.png)
Quét mã này ta có: 12d99aa3a92f1abbb7d40786
Do không có {} nên đây chắc là đoạn giữa
Tương tự thử với Green 6 ta được: SNYK{6947bd4818ffc1768f2
Với Green 7: 5ff8d4e4958d8007a3897}
Ghép 3 đoạn lại ta có flag: SNYK{6947bd4818ffc1768f212d99aa3a92f1abbb7d407865ff8d4e4958d8007a3897}

**[Invisible Ink](https://ctf.snyk.io/challenges#Invisible%20Ink-78)**
Bài này BTC cung cấp đường link [Echo API documentation](http://35.211.53.53:8000/)
và một file source code.
Có một cách là dùng công cụ của Snyk để quét ta có vulnerbility
![photo-2021-10-05-21-05-17](https://i.ibb.co/2vGzxFv/photo-2021-10-05-21-05-17.jpg)
Do BTC cũng cung cấp Source code nên có thể vào đây đọc, có thể thấy nghi nghi có thể google thử viện lodash, nhưng pro @hvn dựng sẵn snyk để quét rồi nên ta có kết quả trên :))
Chú ý đến vul thứ 2.  Đây là PoC của exploit vul này [Prototype Pollution in lodash | Snyk](https://snyk.io/vuln/SNYK-JS-LODASH-450202)
Trong file source code có đoạn check:
``if(output.flag)``
nếu ``true`` sẽ response giá trị của flag
biến output hiện tại đang là:
``output = {}`` nên sẽ không trả về kết quả chúng ta cần
Trong source code có sử dụng Unsafe Object recursive merge
```
merge (target, source) 
	foreach property of source 
	if property exists and is an object on both the target and the source 
		merge(target[property], source[property]) 
	else target[property] = source[property]
```
trong đó target là output còn source là request nên chỉ cần thay request bình thường từ:
`{"message": "ping"}`
sang
`{"constructor": {"prototype": {"flag": true}}}`
khi này thì Object đã bị thêm vào thuộc tính `flag:true`
Do đó `output.flag` sẽ trả về true. Ta có response chứa flag:
SNYK{6a6a6fff87f3cfdca056a077804838d4e87f25f6a11e09627062c06f142b10dd}
![enter image description here](https://i.ibb.co/NmYc1vK/photo-2021-10-05-22-47-33.jpg)