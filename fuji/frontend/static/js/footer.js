$(function(){
    $('.case-logo .logo').mouseenter(function() {
        var className = this.className
        if (className.indexOf('purple') != -1)
            $('.purple').toggleClass('purple green')
        else if (className.indexOf('green') != -1)
            $('.green').toggleClass('green blue')
        else if (className.indexOf('blue') != -1)
            $('.blue').toggleClass('blue red')
        else if (className.indexOf('red'))
            $('.red').toggleClass('red purple')
    })
});