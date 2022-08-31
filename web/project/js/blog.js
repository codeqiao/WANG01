// 针对某一个页面定义一个对象，
// 使用对象空间的方式添加属性和方法
// 在onload事件中执行方法和调用属性

// 针对login页面定义一个对象
var log = {
    startdt: "2022-8-28",
    enddt: "2022-8-28",
    updatedt: "2022-8-28",
    anchor:"cWang"
}

// 由对象派生业务逻辑
log.submit = {
    // 验证某个值是否为空
    check: function (v) {   
        var a = (v=="") ? true : false;
        return a;
    },

    // 自动隐藏error
    autohide: function (obj) {
        setTimeout(function () {
            obj.hide();
        },2000)
    }
}


// 验证内容是否为空
function checkValue() {
    // 获取元素对象并保存在对象中

    var $username = $('#username');
    var $password = $('#password');
    var $err1 = $('#err1');
    var $err2 = $('#err2');
    if (!log.submit.check($username.val()) && !log.submit.check($password.val())) {
        return true;
    } else {
        if (log.submit.check($username.val()) ) {
            $err1.show();
            log.submit.autohide($err1);
        }
        if (log.submit.check($password.val())) {
            $err2.show();
            $err2.hide(5000);
            // log.submit.autohide($err2);
        }
        return false;
    }
}


// 定义一个基于列表页的业务逻辑

var essay = {
    // 生成文章html代码
    generateHtml: function (t, u, p1, p2) {
        var _html = "";
        _html += '<div class="item">';
        _html += '<div class="title">';
        _html += '<h3>'+t+'</h3>';
        _html += '</div>';
        _html += '<div class="con">';
        _html += '<div class="cleft">';
        _html += '<img src="'+u+'" alt="">';
        _html += ' </div>';
        _html += '<div class="cright">';
        _html += '<p class="ptop">';
        _html += p1;
        _html += '</p>';
        _html += '<p class="pbottom">';
        _html += p2;
        _html += '</p>';
        _html += '</div>';
        _html += '</div>';
        _html += '</div>';
        return _html;
    },
    // 将数组中的文章加入到lst中
    appendItem: function (arr) {
        for (var i = 0; i < arr.length; i++){
            var _HTML = this.generateHtml(arr[i].t, arr[i].u, arr[i].p1, arr[i].p2);
            $('#list>.body>.lst').append(_HTML);
        }
    },

}

var arrData = [
    {
        t: "Python语言在人工智能领域中的优势",
        u: "./imgs/computer.png",
        p1: "本文探讨了Python语言在AI领域的优势与运用。谁会成为AI和大数据开发语言？这本已是一个不需要争论的问题。如果说三年前，matlab、Scala、R、Java...",
        p2: "皮皮路 学武无上境 2018-5-13 34567已阅读 9999"
    }, {
        t: "Python语言在人工智能领域中的优势",
        u: "./imgs/computer.png",
        p1: "本文探讨了Python语言在AI领域的优势与运用。谁会成为AI和大数据开发语言？这本已是一个不需要争论的问题。如果说三年前，matlab、Scala、R、Java...",
        p2: "皮皮路 学武无上境 2018-5-13 34567已阅读 9999"
    }, {
        t: "Java语言在人工智能领域中的优势",
        u: "./imgs/computer.png",
        p1: "本文探讨了Python语言在AI领域的优势与运用。谁会成为AI和大数据开发语言？这本已是一个不需要争论的问题。如果说三年前，matlab、Scala、R、Java...",
        p2: "皮皮路 学武无上境 2018-5-13 34567已阅读 9999"
    }
]


var advert = {
    // 生成html代码
    generateHtml: function (src) {
        return _html = '<li> <img src="' + src + '" alt=""></li>"';
    },
    appendAdevert: function (arr) {
        for (var i = 0; i < arr.length; i++){
            var _HTML = this.generateHtml(arr[i]);
            $('#list>.body>.ad>.imglst>ul').append(_HTML);
        }
    },
}

essay.appendItem(arrData);

var arrAdvertSrc = [
    "./imgs/computer.png",
    "./imgs/computer.png",
    "./imgs/computer.png"
]

advert.appendAdevert(arrAdvertSrc)

// 定义一个图片页的业务逻辑对象

var pics1 = {
    generateHtml: function (u, n, t) {
        var _html = "";
        _html += '<div class="item">';
        _html += '<div class="imgs">';
        _html += '<img src="'+u+'" alt="">';
        _html += '<div class="tip">'+n+'</div>';
        _html += '</div>';
        _html += '<div class="title">';
        _html += '<h3>'+t+'</h3>';
        _html += '</div>';
        _html += ' </div>';

        return _html;
    },
    appendAdevert: function (arr) {
        for (var i = 0; i < arr.length; i++){
            var _HTML = this.generateHtml(arr[i].u,arr[i].n,arr[i].t);
            $('#pics>.body').append(_HTML);
        }
    },
}


var arrPics = [{
        u: "./imgs/computer.png",
        n: "喜欢|991",
        t: "爱"
    },{
        u: "./imgs/computer.png",
        n: "喜欢|101",
        t: "家"
    },{
        u: "./imgs/computer.png",
        n: "喜欢|9999",
        t: "春"
    }]

pics1.appendAdevert(arrPics)