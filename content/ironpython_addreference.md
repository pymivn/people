Title: Dùng .NET Framework với IronPython
Date: 2018-06-02
Author: htlcnn
Tags: ironpython, windows, dotnet, reference, dll
Category: Trang chủ
Summary: Giới thiệu cách thêm các công cụ của .NET Framework vào IronPython.
Slug: ironpython-addreference


## Assembly là gì
[Assembly](https://msdn.microsoft.com/en-us/library/ms973231.aspx#assenamesp_topic4) (số nhiều: assemblies) là một file được tạo ra bởi quá trình compile một ứng dụng .NET. Nó có thể có đuôi `.dll` hoặc `.exe`. .NET Framework có sẵn rất nhiều assemblies (chính là thành phần [Class Library trong .NET Framework](https://msdn.microsoft.com/en-us/library/gg145045.aspx)), cũng tương tự như Python có sẵn rất nhiều [standard libraries](https://docs.python.org/3/library/index.html) vậy.

## AddReference .NET Assemblies
Khi lập trình các ngôn ngữ .NET khác như C# hay VB.NET, dùng Visual Studio, muốn sử dụng các công cụ trong .NET Framework thì bạn phải thêm "Reference" vào project browser. IronPython có 1 module hỗ trợ "Add Reference" vào script là `clr`. Các methods Add Reference trong IronPython:
```python
# Sử dụng một trong các methods sau
clr.AddReference
clr.AddReferenceByName
clr.AddReferenceByPartialName
clr.AddReferenceToFile
clr.AddReferenceToFileAndPath
```
`clr.AddReference` nhận vào 1 đối tượng [System.Reflection.Assembly](https://msdn.microsoft.com/en-us/library/system.reflection.assembly(v=vs.110).aspx), hoặc **full name** của assembly (vd `clr.AddReference("System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a")`), hoặc **partial name** của assembly (vd `clr.AddReference("System.Drawing")`). Khi dùng partial name, IronPython sẽ tìm file dll ở trong [Global Assembly Cache (GAC)](https://docs.microsoft.com/en-us/dotnet/framework/app-domains/gac). Mình thường dùng cách thứ 3: truyền vào partial name cho ngắn gọn.
Xem các assemblies đã add ở `clr.References`:
```python
C:\Users\HTL>"c:\Program Files (x86)\IronPython 2.7\ipy.exe"
IronPython 2.7.3 (2.7.0.40) on .NET 4.0.30319.42000 (32-bit)
Type "help", "copyright", "credits" or "license" for more information.
>>> import clr
>>> clr.AddReference("System.Drawing")
>>> clr.References
(<mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089>,
<System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089>,
<IronPython.SQLite, Version=2.7.0.40, Culture=neutral, PublicKeyToken=7f709c5b71
3576e1>,
<IronPython.Wpf, Version=2.7.0.40, Culture=neutral, PublicKeyToken=7f709c5b713576e1>,
<System.Drawing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a>)

>>>
```
Sau khi `AddReference`, phải `import` các namespaces có trong assemblies để sử dụng trong IronPython. Cú pháp import như bình thường:
```python
>>> from System import Drawing
>>> print(Drawing)
Microsoft.Scripting.Actions.NamespaceTracker:System.Drawing
>>>
```
Thắc mắc hay gặp: Mình muốn sử dụng 1 công cụ trong .NET Framework thì biết tên assembly là gì để `AddReference`, biết namespace nào để `import`? Trả lời với từ khóa tìm kiếm: `Tên_công_cụ msdn` (VD [System Environment msdn](http://lmgtfy.com/?s=d&q=System+Environment+msdn)). Dùng phần **Assembly** để `AddReference`, phần **Namespace** để `import`.

Khi chạy ipy.exe, IronPython đã AddReference sẵn tới mscorlib.dll và System.dll [<sup>[1]</sup>](http://ironpython.net/documentation/dotnet/dotnet.html#assemblies-loaded-by-default). Khi đó chỉ việc `import` các namespaces có trong 2 assemblies này mà không phải AddRerence.

## AddReference các Assemblies khác
Ngoài các assemblies có trong .NET Framework, còn có các assemblies khác đi kèm với các phần mềm cài vào Windows, hoặc assemblies được compiled từ chính IronPython. Cú pháp AddReference tương tự như trên, với lưu ý là `AddReference` khi đó sẽ tìm assemblies trong GAC hoặc `sys.path`. Nếu không muốn append đường dẫn tới folder chứa file .dll thì có thể dùng `AddReferenceToFileAndPath`. Phải chạy đúng phiên bản IronPython 32bit/64bit tương ứng với [Target Platform](https://msdn.microsoft.com/en-us/library/hh264221.aspx#Target%20Platform) mà file assembly được compiled.

Ví dụ file `RevitAPI.dll` được compiled với Target Platform là x64 (64-bit), nếu chạy `ipy.exe` (32-bit) sẽ không `AddReference` được:
```python
C:\Users\HTL>"C:\Program Files (x86)\IronPython 2.7\ipy.exe"
IronPython 2.7.3 (2.7.0.40) on .NET 4.0.30319.42000 (32-bit)
Type "help", "copyright", "credits" or "license" for more information.
>>> import clr
>>> import sys
>>> sys.path.append(r'C:\Program Files\Autodesk\Revit 2018')
>>> clr.AddReference('RevitAPI')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IOError: System.IO.IOException: Could not add reference to assembly RevitAPI
   at IronPython.Runtime.ClrModule.AddReference(CodeContext context, String name
)
   at IronPython.Runtime.ClrModule.AddReference(CodeContext context, Object refe
rence)
   at IronPython.Runtime.ClrModule.AddReference(CodeContext context, Object[] re
ferences)
   at Microsoft.Scripting.Interpreter.ActionCallInstruction`2.Run(InterpretedFra
me frame)
   at Microsoft.Scripting.Interpreter.Interpreter.Run(InterpretedFrame frame)
   at Microsoft.Scripting.Interpreter.LightLambda.Run4[T0,T1,T2,T3,TRet](T0 arg0
, T1 arg1, T2 arg2, T3 arg3)
   at System.Dynamic.UpdateDelegates.UpdateAndExecute3[T0,T1,T2,TRet](CallSite s
ite, T0 arg0, T1 arg1, T2 arg2)
   at Microsoft.Scripting.Interpreter.FuncCallInstruction`6.Run(InterpretedFrame
 frame)
   at Microsoft.Scripting.Interpreter.Interpreter.Run(InterpretedFrame frame)
   at Microsoft.Scripting.Interpreter.LightLambda.Run4[T0,T1,T2,T3,TRet](T0 arg0
, T1 arg1, T2 arg2, T3 arg3)
   at IronPython.Compiler.Ast.CallExpression.Invoke1Instruction.Run(InterpretedF
rame frame)
   at Microsoft.Scripting.Interpreter.Interpreter.Run(InterpretedFrame frame)
   at Microsoft.Scripting.Interpreter.LightLambda.Run2[T0,T1,TRet](T0 arg0, T1 a
rg1)
   at IronPython.Compiler.PythonScriptCode.RunWorker(CodeContext ctx)
   at IronPython.Compiler.PythonScriptCode.Run(Scope scope)
   at IronPython.Hosting.PythonCommandLine.<>c__DisplayClass1.<RunOneInteraction
>b__0()
>>>
```

Mà phải dùng `ipy64.exe` để `AddReference`:
```python
C:\Users\HTL>"C:\Program Files (x86)\IronPython 2.7\ipy64.exe"
IronPython 2.7.3 (2.7.0.40) on .NET 4.0.30319.42000 (64-bit)
Type "help", "copyright", "credits" or "license" for more information.
>>> import clr
>>> import sys
>>> sys.path
['.', 'C:\\Program Files (x86)\\IronPython 2.7\\Lib',
 'C:\\Program Files (x86)\\IronPython 2.7\\DLLs',
 'C:\\Program Files (x86)\\IronPython 2.7',
 'C:\\Program Files (x86)\\IronPython 2.7\\lib\\site-packages']
>>> sys.path.append(r'C:\Program Files\Autodesk\Revit 2018')
>>> clr.AddReference('RevitAPI')
>>> from Autodesk.Revit.DB import Wall
>>> Wall
<type 'Wall'>
>>>
```