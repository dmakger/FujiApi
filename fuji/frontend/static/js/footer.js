$(function(){
    $('footer .case-logo .logo').mouseenter(function() {
        var className = this.className
        if (className.indexOf('purple') != -1)
            $(this).toggleClass('purple green')
        else if (className.indexOf('green') != -1)
            $(this).toggleClass('green blue')
        else if (className.indexOf('blue') != -1)
            $(this).toggleClass('blue red')
        else if (className.indexOf('red'))
            $(this).toggleClass('red purple')
    })
});