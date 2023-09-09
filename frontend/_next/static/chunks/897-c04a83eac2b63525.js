(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[897],{5202:function(){!function(){"use strict";function e(e){var t=!0,n=!1,r=null,i={text:!0,search:!0,url:!0,tel:!0,email:!0,password:!0,number:!0,date:!0,month:!0,week:!0,time:!0,datetime:!0,"datetime-local":!0};function a(e){return!!e&&e!==document&&"HTML"!==e.nodeName&&"BODY"!==e.nodeName&&"classList"in e&&"contains"in e.classList}function o(e){e.classList.contains("focus-visible")||(e.classList.add("focus-visible"),e.setAttribute("data-focus-visible-added",""))}function s(e){t=!1}function c(){document.addEventListener("mousemove",l),document.addEventListener("mousedown",l),document.addEventListener("mouseup",l),document.addEventListener("pointermove",l),document.addEventListener("pointerdown",l),document.addEventListener("pointerup",l),document.addEventListener("touchmove",l),document.addEventListener("touchstart",l),document.addEventListener("touchend",l)}function l(e){e.target.nodeName&&"html"===e.target.nodeName.toLowerCase()||(t=!1,document.removeEventListener("mousemove",l),document.removeEventListener("mousedown",l),document.removeEventListener("mouseup",l),document.removeEventListener("pointermove",l),document.removeEventListener("pointerdown",l),document.removeEventListener("pointerup",l),document.removeEventListener("touchmove",l),document.removeEventListener("touchstart",l),document.removeEventListener("touchend",l))}document.addEventListener("keydown",function(n){n.metaKey||n.altKey||n.ctrlKey||(a(e.activeElement)&&o(e.activeElement),t=!0)},!0),document.addEventListener("mousedown",s,!0),document.addEventListener("pointerdown",s,!0),document.addEventListener("touchstart",s,!0),document.addEventListener("visibilitychange",function(e){"hidden"===document.visibilityState&&(n&&(t=!0),c())},!0),c(),e.addEventListener("focus",function(e){var n,r,s;a(e.target)&&(t||(r=(n=e.target).type,"INPUT"===(s=n.tagName)&&i[r]&&!n.readOnly||"TEXTAREA"===s&&!n.readOnly||n.isContentEditable))&&o(e.target)},!0),e.addEventListener("blur",function(e){if(a(e.target)){var t;(e.target.classList.contains("focus-visible")||e.target.hasAttribute("data-focus-visible-added"))&&(n=!0,window.clearTimeout(r),r=window.setTimeout(function(){n=!1},100),(t=e.target).hasAttribute("data-focus-visible-added")&&(t.classList.remove("focus-visible"),t.removeAttribute("data-focus-visible-added")))}},!0),e.nodeType===Node.DOCUMENT_FRAGMENT_NODE&&e.host?e.host.setAttribute("data-js-focus-visible",""):e.nodeType===Node.DOCUMENT_NODE&&(document.documentElement.classList.add("js-focus-visible"),document.documentElement.setAttribute("data-js-focus-visible",""))}if("undefined"!=typeof window&&"undefined"!=typeof document){var t;window.applyFocusVisiblePolyfill=e;try{t=new CustomEvent("focus-visible-polyfill-ready")}catch(e){(t=document.createEvent("CustomEvent")).initCustomEvent("focus-visible-polyfill-ready",!1,!1,{})}window.dispatchEvent(t)}"undefined"!=typeof document&&e(document)}()},9008:function(e,t,n){e.exports=n(2636)},5698:function(e,t,n){"use strict";n.d(t,{z:function(){return p}});var r=n(7294),[i,a]=(0,n(5227).k)({strict:!1,name:"ButtonGroupContext"}),o=n(2504),s=n(5432),c=n(5893);function l(e){let{children:t,className:n,...i}=e,a=(0,r.isValidElement)(t)?(0,r.cloneElement)(t,{"aria-hidden":!0,focusable:!1}):t,l=(0,s.cx)("chakra-button__icon",n);return(0,c.jsx)(o.m.span,{display:"inline-flex",alignSelf:"center",flexShrink:0,...i,className:l,children:a})}l.displayName="ButtonIcon";var d=n(295);function u(e){let{label:t,placement:n,spacing:i="0.5rem",children:a=(0,c.jsx)(d.$,{color:"currentColor",width:"1em",height:"1em"}),className:l,__css:u,...m}=e,f=(0,s.cx)("chakra-button__spinner",l),v="start"===n?"marginEnd":"marginStart",p=(0,r.useMemo)(()=>({display:"flex",alignItems:"center",position:t?"relative":"absolute",[v]:t?i:0,fontSize:"1em",lineHeight:"normal",...u}),[u,t,v,i]);return(0,c.jsx)(o.m.div,{className:f,...m,__css:p,children:a})}u.displayName="ButtonSpinner";var m=n(5059),f=n(1628),v=n(3179),p=(0,m.G)((e,t)=>{let n=a(),i=(0,f.mq)("Button",{...n,...e}),{isDisabled:l=null==n?void 0:n.isDisabled,isLoading:d,isActive:m,children:p,leftIcon:g,rightIcon:x,loadingText:y,iconSpacing:b="0.5rem",type:E,spinner:N,spinnerPlacement:L="start",className:j,as:_,...w}=(0,v.Lr)(e),k=(0,r.useMemo)(()=>{let e={...null==i?void 0:i._focus,zIndex:1};return{display:"inline-flex",appearance:"none",alignItems:"center",justifyContent:"center",userSelect:"none",position:"relative",whiteSpace:"nowrap",verticalAlign:"middle",outline:"none",...i,...!!n&&{_focus:e}}},[i,n]),{ref:C,type:S}=function(e){let[t,n]=(0,r.useState)(!e),i=(0,r.useCallback)(e=>{e&&n("BUTTON"===e.tagName)},[]);return{ref:i,type:t?"button":void 0}}(_),T={rightIcon:x,leftIcon:g,iconSpacing:b,children:p};return(0,c.jsxs)(o.m.button,{ref:function(...e){return(0,r.useMemo)(()=>(function(...e){return t=>{e.forEach(e=>{!function(e,t){if(null!=e){if("function"==typeof e){e(t);return}try{e.current=t}catch(n){throw Error(`Cannot assign value '${t}' to ref '${e}'`)}}}(e,t)})}})(...e),e)}(t,C),as:_,type:null!=E?E:S,"data-active":(0,s.PB)(m),"data-loading":(0,s.PB)(d),__css:k,className:(0,s.cx)("chakra-button",j),...w,disabled:l||d,children:[d&&"start"===L&&(0,c.jsx)(u,{className:"chakra-button__spinner--start",label:y,placement:"start",spacing:b,children:N}),d?y||(0,c.jsx)(o.m.span,{opacity:0,children:(0,c.jsx)(h,{...T})}):(0,c.jsx)(h,{...T}),d&&"end"===L&&(0,c.jsx)(u,{className:"chakra-button__spinner--end",label:y,placement:"end",spacing:b,children:N})]})});function h(e){let{leftIcon:t,rightIcon:n,children:r,iconSpacing:i}=e;return(0,c.jsxs)(c.Fragment,{children:[t&&(0,c.jsx)(l,{marginEnd:i,children:t}),r,n&&(0,c.jsx)(l,{marginStart:i,children:n})]})}p.displayName="Button"},78:function(e,t,n){"use strict";n.d(t,{I:function(){return s}});var r=n(6877),i=n(5059),a=n(7294),o=n(5893);function s(e){let{viewBox:t="0 0 24 24",d:n,displayName:s,defaultProps:c={}}=e,l=a.Children.toArray(e.path),d=(0,i.G)((e,i)=>(0,o.jsx)(r.J,{ref:i,viewBox:t,...c,...e,children:l.length?l:(0,o.jsx)("path",{fill:"currentColor",d:n})}));return d.displayName=s,d}},2774:function(e,t,n){"use strict";n.d(t,{V:function(){return a}});var r=n(78),i=n(5893),a=(0,r.I)({displayName:"MinusIcon",path:(0,i.jsx)("g",{fill:"currentColor",children:(0,i.jsx)("rect",{height:"4",width:"20",x:"2",y:"10"})})})},1785:function(e,t,n){"use strict";n.d(t,{d:function(){return r}});var r=(0,n(78).I)({d:"M0,12a1.5,1.5,0,0,0,1.5,1.5h8.75a.25.25,0,0,1,.25.25V22.5a1.5,1.5,0,0,0,3,0V13.75a.25.25,0,0,1,.25-.25H22.5a1.5,1.5,0,0,0,0-3H13.75a.25.25,0,0,1-.25-.25V1.5a1.5,1.5,0,0,0-3,0v8.75a.25.25,0,0,1-.25.25H1.5A1.5,1.5,0,0,0,0,12Z",displayName:"AddIcon"})},4416:function(e,t,n){"use strict";n.d(t,{E:function(){return d}});var r=n(5059),i=n(5893),a=(0,r.G)(function(e,t){let{htmlWidth:n,htmlHeight:r,alt:a,...o}=e;return(0,i.jsx)("img",{width:n,height:r,ref:t,alt:a,...o})});a.displayName="NativeImage";var o=n(6245),s=n(7294),c=(e,t)=>"loaded"!==e&&"beforeLoadOrError"===t||"failed"===e&&"onError"===t,l=n(2504),d=(0,r.G)(function(e,t){let{fallbackSrc:n,fallback:r,src:d,srcSet:u,align:m,fit:f,loading:v,ignoreFallback:p,crossOrigin:h,fallbackStrategy:g="beforeLoadOrError",referrerPolicy:x,...y}=e,b=null!=v||p||!(void 0!==n||void 0!==r),E=function(e){let{loading:t,src:n,srcSet:r,onLoad:i,onError:a,crossOrigin:c,sizes:l,ignoreFallback:d}=e,[u,m]=(0,s.useState)("pending");(0,s.useEffect)(()=>{m(n?"loading":"pending")},[n]);let f=(0,s.useRef)(),v=(0,s.useCallback)(()=>{if(!n)return;p();let e=new Image;e.src=n,c&&(e.crossOrigin=c),r&&(e.srcset=r),l&&(e.sizes=l),t&&(e.loading=t),e.onload=e=>{p(),m("loaded"),null==i||i(e)},e.onerror=e=>{p(),m("failed"),null==a||a(e)},f.current=e},[n,c,r,l,i,a,t]),p=()=>{f.current&&(f.current.onload=null,f.current.onerror=null,f.current=null)};return(0,o.G)(()=>{if(!d)return"loading"===u&&v(),()=>{p()}},[u,v,d]),d?"loaded":u}({...e,crossOrigin:h,ignoreFallback:b}),N=c(E,g),L={ref:t,objectFit:f,objectPosition:m,...b?y:function(e,t=[]){let n=Object.assign({},e);for(let e of t)e in n&&delete n[e];return n}(y,["onError","onLoad"])};return N?r||(0,i.jsx)(l.m.img,{as:a,className:"chakra-image__placeholder",src:n,...L}):(0,i.jsx)(l.m.img,{as:a,src:d,srcSet:u,crossOrigin:h,loading:v,referrerPolicy:x,className:"chakra-image",...L})});d.displayName="Image"},7754:function(e,t,n){"use strict";n.d(t,{M:function(){return o}});var r=n(2504),i=n(5059),a=n(5893),o=(0,r.m)("div",{baseStyle:{display:"flex",alignItems:"center",justifyContent:"center"}});o.displayName="Center";var s={horizontal:{insetStart:"50%",transform:"translateX(-50%)"},vertical:{top:"50%",transform:"translateY(-50%)"},both:{insetStart:"50%",top:"50%",transform:"translate(-50%, -50%)"}};(0,i.G)(function(e,t){let{axis:n="both",...i}=e;return(0,a.jsx)(r.m.div,{ref:t,__css:s[n],...i,position:"absolute"})})},1689:function(e,t,n){"use strict";n.d(t,{C:function(){return l}});var r=n(5059),i=n(1628),a=n(3179),o=n(2504),s=n(5432),c=n(5893),l=(0,r.G)(function(e,t){let n=(0,i.mq)("Badge",e),{className:r,...l}=(0,a.Lr)(e);return(0,c.jsx)(o.m.span,{ref:t,className:(0,s.cx)("chakra-badge",e.className),...l,__css:{display:"inline-block",whiteSpace:"nowrap",verticalAlign:"middle",...n}})});l.displayName="Badge"},4641:function(e,t,n){"use strict";n.d(t,{U:function(){return o}});var r=n(7073),i=n(5059),a=n(5893),o=(0,i.G)((e,t)=>(0,a.jsx)(r.K,{align:"center",...e,direction:"row",ref:t}));o.displayName="HStack"},1669:function(e,t,n){"use strict";n.d(t,{g:function(){return o}});var r=n(7073),i=n(5059),a=n(5893),o=(0,i.G)((e,t)=>(0,a.jsx)(r.K,{align:"center",...e,direction:"column",ref:t}));o.displayName="VStack"},7073:function(e,t,n){"use strict";n.d(t,{K:function(){return u}});var r=n(2504),i=n(5893),a=e=>(0,i.jsx)(r.m.div,{className:"chakra-stack__item",...e,__css:{display:"inline-block",flex:"0 0 auto",minWidth:0,...e.__css}});a.displayName="StackItem";var o=n(5432);function s(e,t){return Array.isArray(e)?e.map(e=>null===e?null:t(e)):(0,o.Kn)(e)?Object.keys(e).reduce((n,r)=>(n[r]=t(e[r]),n),{}):null!=e?t(e):null}Object.freeze(["base","sm","md","lg","xl","2xl"]);var c="& > *:not(style) ~ *:not(style)",l=n(5059),d=n(7294),u=(0,l.G)((e,t)=>{let{isInline:n,direction:l,align:u,justify:m,spacing:f="0.5rem",wrap:v,children:p,divider:h,className:g,shouldWrapChildren:x,...y}=e,b=n?"row":null!=l?l:"column",E=(0,d.useMemo)(()=>(function(e){let{spacing:t,direction:n}=e,r={column:{marginTop:t,marginEnd:0,marginBottom:0,marginStart:0},row:{marginTop:0,marginEnd:0,marginBottom:0,marginStart:t},"column-reverse":{marginTop:0,marginEnd:0,marginBottom:t,marginStart:0},"row-reverse":{marginTop:0,marginEnd:t,marginBottom:0,marginStart:0}};return{flexDirection:n,[c]:s(n,e=>r[e])}})({direction:b,spacing:f}),[b,f]),N=(0,d.useMemo)(()=>(function(e){let{spacing:t,direction:n}=e,r={column:{my:t,mx:0,borderLeftWidth:0,borderBottomWidth:"1px"},"column-reverse":{my:t,mx:0,borderLeftWidth:0,borderBottomWidth:"1px"},row:{mx:t,my:0,borderLeftWidth:"1px",borderBottomWidth:0},"row-reverse":{mx:t,my:0,borderLeftWidth:"1px",borderBottomWidth:0}};return{"&":s(n,e=>r[e])}})({spacing:f,direction:b}),[f,b]),L=!!h,j=!x&&!L,_=(0,d.useMemo)(()=>{let e=d.Children.toArray(p).filter(e=>(0,d.isValidElement)(e));return j?e:e.map((t,n)=>{let r=void 0!==t.key?t.key:n,o=n+1===e.length,s=(0,i.jsx)(a,{children:t},r),c=x?s:t;if(!L)return c;let l=(0,d.cloneElement)(h,{__css:N});return(0,i.jsxs)(d.Fragment,{children:[c,o?null:l]},r)})},[h,N,L,j,x,p]),w=(0,o.cx)("chakra-stack",g);return(0,i.jsx)(r.m.div,{ref:t,display:"flex",alignItems:u,justifyContent:m,flexDirection:E.flexDirection,flexWrap:v,className:w,__css:L?{}:{[c]:E[c]},...y,children:_})});u.displayName="Stack"},9564:function(e,t,n){"use strict";n.d(t,{x:function(){return l}});var r=n(5059),i=n(1628),a=n(3179),o=n(2504),s=n(5432),c=n(5893),l=(0,r.G)(function(e,t){let n=(0,i.mq)("Text",e),{className:r,align:l,decoration:d,casing:u,...m}=(0,a.Lr)(e),f=function(e){let t=Object.assign({},e);for(let e in t)void 0===t[e]&&delete t[e];return t}({textAlign:e.align,textDecoration:e.decoration,textTransform:e.casing});return(0,c.jsx)(o.m.p,{ref:t,className:(0,s.cx)("chakra-text",e.className),...f,...m,__css:n})});l.displayName="Text"},6979:function(e,t,n){"use strict";n.d(t,{W:function(){return l}});var r=n(5059),i=n(3179),a=n(1628),o=n(2504),s=n(5432),c=n(5893),l=(0,r.G)(function(e,t){let{className:n,centerContent:r,...l}=(0,i.Lr)(e),d=(0,a.mq)("Container",e);return(0,c.jsx)(o.m.div,{ref:t,className:(0,s.cx)("chakra-container",n),...l,__css:{...d,...r&&{display:"flex",flexDirection:"column",alignItems:"center"}}})});l.displayName="Container"}}]);