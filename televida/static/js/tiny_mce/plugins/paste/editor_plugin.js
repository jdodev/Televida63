(function(){var a=tinymce.each;tinymce.create("tinymce.plugins.PastePlugin",{init:function(c,d){var e=this,b;e.editor=c;e.url=d;e.onPreProcess=new tinymce.util.Dispatcher(e);e.onPostProcess=new tinymce.util.Dispatcher(e);e.onPreProcess.add(e._preProcess);e.onPostProcess.add(e._postProcess);e.onPreProcess.add(function(h,i){c.execCallback("paste_preprocess",h,i)});e.onPostProcess.add(function(h,i){c.execCallback("paste_postprocess",h,i)});function g(i){var k=c.dom,j={content:i};e.onPreProcess.dispatch(e,j);j.node=k.create("div",0,j.content);e.onPostProcess.dispatch(e,j);j.content=c.serializer.serialize(j.node,{getInner:1});if(/<(p|h[1-6]|ul|ol)/.test(j.content)){e._insertBlockContent(c,k,j.content)}else{e._insert(j.content)}}c.addCommand("mceInsertClipboardContent",function(i,h){g(h)});function f(l){var p,k,i,j=c.selection,o=c.dom,h=c.getBody(),m;if(o.get("_mcePaste")){return}p=o.add(h,"div",{id:"_mcePaste"},"&nbsp;");if(h!=c.getDoc().body){m=o.getPos(c.selection.getStart(),h).y}else{m=h.scrollTop}o.setStyles(p,{position:"absolute",left:-10000,top:m,width:1,height:1,overflow:"hidden"});if(tinymce.isIE){i=o.doc.body.createTextRange();i.moveToElementText(p);i.execCommand("Paste");o.remove(p);g(p.innerHTML);return tinymce.dom.Event.cancel(l)}else{k=c.selection.getRng();p=p.firstChild;i=c.getDoc().createRange();i.setStart(p,0);i.setEnd(p,1);j.setRng(i);window.setTimeout(function(){var r=o.get("_mcePaste"),q;r.id="_mceRemoved";o.remove(r);r=o.get("_mcePaste")||r;q=(o.select("> span.Apple-style-span div",r)[0]||o.select("> span.Apple-style-span",r)[0]||r).innerHTML;o.remove(r);if(k){j.setRng(k)}g(q)},0)}}if(c.getParam("paste_auto_cleanup_on_paste",true)){if(tinymce.isOpera||/Firefox\/2/.test(navigator.userAgent)){c.onKeyDown.add(function(h,i){if(((tinymce.isMac?i.metaKey:i.ctrlKey)&&i.keyCode==86)||(i.shiftKey&&i.keyCode==45)){f(i)}})}else{c.onPaste.addToTop(function(h,i){return f(i)})}}e._legacySupport()},getInfo:function(){return{longname:"Paste text/word",author:"Moxiecode Systems AB",authorurl:"http://tinymce.moxiecode.com",infourl:"http://wiki.moxiecode.com/index.php/TinyMCE:Plugins/paste",version:tinymce.majorVersion+"."+tinymce.minorVersion}},_preProcess:function(c,e){var b=e.content,d;function d(f){a(f,function(g){if(g.constructor==RegExp){b=b.replace(g,"")}else{b=b.replace(g[0],g[1])}})}d([/^\s*(&nbsp;)+/g,/(&nbsp;|<br[^>]*>)+\s*$/g]);if(/(class=\"?Mso|style=\"[^\"]*\bmso\-|w:WordDocument)/.test(b)){e.wordContent=true;d([/<!--[\s\S]+?-->/gi,/<\/?(img|font|meta|link|style|span|div|v:\w+)[^>]*>/gi,/<\\?\?xml[^>]*>/gi,/<\/?o:[^>]*>/gi,/ (id|name|class|language|type|on\w+|v:\w+)=\"([^\"]*)\"/gi,/ (id|name|class|language|type|on\w+|v:\w+)=(\w+)/gi,[/<(\/?)s>/gi,"<$1strike>"],/<script[^>]+>[\s\S]*?<\/script>/gi,[/&nbsp;/g,"\u00a0"]])}e.content=b},_postProcess:function(c,e){var b=this,d=b.editor.dom;if(e.wordContent){a(d.select("a",e.node),function(f){if(!f.href||f.href.indexOf("#_Toc")!=-1){d.remove(f,1)}});if(b.editor.getParam("paste_convert_middot_lists",true)){b._convertLists(c,e)}a(d.select("*",e.node),function(f){d.setAttrib(f,"style","")})}if(tinymce.isWebKit){a(d.select("*",e.node),function(f){f.removeAttribute("mce_style")})}},_convertLists:function(e,c){var g=e.editor.dom,f,i,b=-1,d,j=[],h;a(g.select("p",c.node),function(q){var m,r="",o,n,k,l;for(m=q.firstChild;m&&m.nodeType==3;m=m.nextSibling){r+=m.nodeValue}if(/^[\u2022\u00b7\u00a7\u00d8o]\s*\u00a0\u00a0*/.test(r)){o="ul"}if(/^[\s\S]*\w+\.[\s\S]*\u00a0{2,}/.test(r)){o="ol"}if(o){d=parseFloat(q.style.marginLeft||0);if(d>b){j.push(d)}if(!f||o!=h){f=g.create(o);g.insertAfter(f,q)}else{if(d>b){f=i.appendChild(g.create(o))}else{if(d<b){k=tinymce.inArray(j,d);l=g.getParents(f.parentNode,o);f=l[l.length-1-k]||f}}}if(o=="ul"){n=q.innerHTML.replace(/^[\u2022\u00b7\u00a7\u00d8o]\s*(&nbsp;|\u00a0)+\s*/,"")}else{n=q.innerHTML.replace(/^[\s\S]*\w+\.(&nbsp;|\u00a0)+\s*/,"")}i=f.appendChild(g.create("li",0,n));g.remove(q);b=d;h=o}else{f=b=0}})},_insertBlockContent:function(h,e,i){var c,g,d=h.selection,m,j,b,k,f;function l(p){var o;if(tinymce.isIE){o=h.getDoc().body.createTextRange();o.moveToElementText(p);o.collapse(false);o.select()}else{d.select(p,1);d.collapse(false)}}this._insert('<span id="_marker">&nbsp;</span>',1);g=e.get("_marker");c=e.getParent(g,"p,h1,h2,h3,h4,h5,h6,ul,ol");if(c){g=e.split(c,g);a(e.create("div",0,i).childNodes,function(o){m=g.parentNode.insertBefore(o.cloneNode(true),g)});l(m)}else{e.setOuterHTML(g,i);d.select(h.getBody(),1);d.collapse(0)}e.remove("_marker");j=d.getStart();b=e.getViewPort(h.getWin());k=h.dom.getPos(j).y;f=j.clientHeight;if(k<b.y||k+f>b.y+b.h){h.getDoc().body.scrollTop=k<b.y?k:k-b.h+25}},_insert:function(d,b){var c=this.editor;c.execCommand("Delete");c.execCommand(tinymce.isGecko?"insertHTML":"mceInsertContent",false,d,{skip_undo:b})},_legacySupport:function(){var c=this,b=c.editor;a(["mcePasteText","mcePasteWord"],function(d){b.addCommand(d,function(){b.windowManager.open({file:c.url+(d=="mcePasteText"?"/pastetext.htm":"/pasteword.htm"),width:450,height:400,inline:1})})});b.addButton("pastetext",{title:"paste.paste_text_desc",cmd:"mcePasteText"});b.addButton("pasteword",{title:"paste.paste_word_desc",cmd:"mcePasteWord"});b.addButton("selectall",{title:"paste.selectall_desc",cmd:"selectall"})}});tinymce.PluginManager.add("paste",tinymce.plugins.PastePlugin)})();