# 使用方式

> 绑定元素 内嵌 外部引入的方式进行执行

```js
    <div>
        <button onclick="alert('输入有误！')">点击</button>
    </div>

    <script>
        alert("我是顶部")
    </script>

    <script src="./01.js"></script>

```

语句的概念是以;为结束
# 常用的输入语句

```js
    alert(); -- 普通页面的弹窗
    prompt(); -- 接收用户输入的弹窗，返回用户输入的内容,会有一个返回值
    console.log(); -- 控制台输出，常用于调试
    document.write("<h1>Hello</h1>"); -- 实现动态在页面中写入内容

```

# DOM事件处理
## 事件函数分类

> 鼠标事件

```js
    onclick     //单击
    ondblclick  //双击
    onmouseover //鼠标移入
    onmouseout  //鼠标移出
    onmousemove //鼠标移动
```

> 文档或元素加载完毕

```js
    onload      //元素或文档加载完毕
```
> 表单控件状态监听
```js
    onfocus     //文本框获取焦点
    onblur      //文本框失去焦点
    oninput     //实时监听输入
    onchange    //两次输入内容发生变化时触发，或元素状态改变时触发
    onsubmit    //form元素监听，点击提交按钮后触发，通过返回值控制数据是否可以发送给服务器
```

## 事件绑定方式

> 内联方式
```js
    <button onclick="alert('输入有误！')">点击</button>
```
> 动态绑定：获取元素结点，动态添加事件
```js
    btn.onclick = function(){

    }
```

# 运算符
```js
    ===     //完全相等，类型相同值也相同
    !==     //不全等

```

# 数组
```js
    var a = []
    a.push(参数)    在数组末尾插入数据返回数组长度
    a.pop()         删除末尾数据
    a.unshift(参数) 在数组最前面插入元素
    a.shift()       删除最前面元素
    a.toString()    转化为字符串
    a.sort()        排序
    a.reserve       逆置
```

# 函数的使用方法
> 匿名函数的使用方法:
```js
    // 定义一个带参数匿名函数
    (function(name,age){

    })('wang',19)   调用匿名函数
```

> 目前主流写法(JSON格式函数)
```js
    var log={
        ab:function(){
            return 'ok'
        },
        cd:function(){
            return 'no'
        }
    }
```



# 常用函数
```js
    var num = 3.1415926
    var res = num.toFixed(2) // 保留两位有效数字

    num.toString(); //强制转换成字符型
    
    Number(param);  //字符转换为数字，转换失败返回 NaN

    parseInt(param);    //从数据中截取为整数部分

    parseFloat(param);  //截取全部

    setAttribute('src','路径')  //设置图片路径的函数

    confirm("你确定要关闭吗？") //询问对话框

    // 定时器方法
        // 间歇性定时器
        var timerID = setInterval(function（函数）,interval（间隔时间）);
        // 关闭定时器
        clearInterval(timerID);

        // 一次性定时器
        var timerID = setTimeout(function（函数）,timeout（多久后执行）);
        // 关闭定时器
        closeTimeout(timerID);

```

# 绑定事件

> 在js属性中
```js
    // 先获取拖动元素的对象，并保存在变量a中
    var a = document.getElementById('num')
    // 绑定值的改变事件
    a.onchange=function(){

    }
```


# 事件
```js
    onclick 单机事件
    oninput 输入事件
```

# 文本对象
```js
    innerText   //元素内容
    innerHTML   //元素内的嵌入代码
    value       //输入框输入的值

```

# 注意
```
    通过class寻找到的对象是一个列表
```




# JQ框架
JQ是JS的工具库。对原生的DOM操作、事件处理、包括数据处理和Ajax技术等进行封装，提供更完善，更便捷的方法

### 工厂函数-$()
> 该函数用于获取元素结点，创建元素结点或将原生js对象转化为jq对象，返回jq对象。jq对象实际是一个类数组对象，包含了一系列jq操作的方法

> 1、基础选择器
```
    标签选择器  $(h1)
    ID选择器    $(#d1)
    类选择器    $(.c1)
    群组选择器  $(body,h1,p)
```
> 2、层级选择器

```
    后代选择器  $('div .c1')
    子代选择器  $('div>span')
    相邻兄弟选择器  $('h1+p')   匹配满足选择器1后面的第一个兄弟元素，同时要求兄弟元素满足选择器2
    通用兄弟选择器  $('h1~h2')  匹配选择器1后面所有满足选择器2的兄弟元素
```

> 3、过滤选择器（需要结合其他选择器使用）

```
    :first
        匹配第一个元素，例 $('p:first')
    :last
        匹配最后一个元素
    :odd
        匹配奇数下表的元素
    :even
        匹配偶数下标的元素
    :eq(index)
        匹配指定下标的元素
    :lt(index)
        匹配下标小于index的元素
    :gt(index)
        匹配下标大于index的元素
    :not(选择器)
        否定筛选，除去（）中的选择器，其他元素

```
> 4、属性选择器

```
    [attrName]  匹配包含指定属性的元素
    [attrName=value]/[attrName='value'] 匹配属性名=属性值的元素
    [attrName^=value]   匹配属性值以指定字符开头的元素
    [attrName$=value]   匹配属性值以指定字符结尾的元素
    [attrName*=vlaue]   匹配属性值包含指定字符的元素
```
> 5、子元素过滤选择器

```
    :first-child    匹配第一个选择器
    :last-child     匹配最后一个元素
    :nth-child(n)   匹配第n个元素(n从1开始计数)
```

### 操作标签属性
```
    1、attr('attrName','value')
    2、prop()   读取或者设置表单元素属性时使用，这个函数会监听表单元素的状态
    3、removeAttr('attrName')   移出属性
```

### 操作标签样式
```js
    addClass('className')   //添加指定的类名
    removeClass('className')//移除指定的类型，如果省略参数，表示清空class属性值
    toggleClass('className')//结合用户行为，实现动态切换类名，如果当前元素存在指定类名，则移出，不存在则添加
```

### 解决权重不够的问题

> background-color: red !important;