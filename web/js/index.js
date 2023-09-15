console.log("此项目为开源项目，如果对该项目有建议，欢迎来 https://github.com/ky0ha/class_ending 提交 pr")

document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('myForm');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // 阻止默认表单提交行为

        var sname = document.getElementById('sname').value;
        var cname = document.getElementById('day').value + ' ' + document.getElementById('time').value;
        var date = document.getElementById('date').value;
        var tname = document.getElementById('tname').value;
        var school = document.getElementById('school').value;

        // 在此处可以执行提交表单数据的操作，例如使用 AJAX 发送到服务器
        // 创建 XHR 对象
        var xhr = new XMLHttpRequest();
        xhr.open('POST', 'http://ky0ha.com:8000/api/ending'); // 指定请求的 URL
        xhr.setRequestHeader('Content-Type', 'application/json'); // 设置请求头
        xhr.setRequestHeader('Access-Control-Allow-Origin', true); // 设置请求头

        // 监听 XHR 的状态变化
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    // 请求成功处理逻辑
                    console.log(xhr.responseText);

                    // 获取响应头信息
                    var link = document.createElement('a');
                    link.href = `${xhr.responseURL}/temp.jpg`
                    link.download = ''; // 指定下载的文件名

                    // 触发点击事件下载文件
                    link.click();
                    link.remove();

                } else {
                    // 请求失败处理逻辑
                    console.error('请求失败:', xhr.status);
                }
            }
        };


        // 将表单数据转换为 JSON 格式
        var formData = {
            sname: sname,
            cname: cname,
            date: date,
            tname: tname,
            school: school
        };
        var jsonData = JSON.stringify(formData);

        // 发送请求
        xhr.send(jsonData);

        // 清空表单字段
        form.reset();
    });
});