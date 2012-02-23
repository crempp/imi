imi = {
    
}


/**
 * Dojo initialization
 *
*/
DojoBoot = {
    stageOne: function(){
        try{
            dojo.config.parseOnLoad = true;
            dojo.config.dojoBlankHtmlUrl = 'http://media.lapinlabs.com/blank.html';
        } catch (err) {
            loaderModal.message("<p>Could not initiate boot</p><p>["+err+"]</p>",'error');
        }
    },
    stageTwo : function(){
        loaderModal.load({message:"Loading Dojo requirements"});
        console.log("Loading Dojo requirements");
        try{
            dojo.require("dijit.Declaration");
		    dojo.require("dojo.parser");
            dojo.require("dijit.Dialog");
            dojo.require("dijit.layout.BorderContainer");
            dojo.require("dijit.layout.ContentPane");
            //dojo.require("dijit.form.Button");
            dojo.require("dojo.data.ItemFileReadStore");
            dojo.require("dijit.tree.ForestStoreModel");
            dojo.require("dijit.Tree");
            
        } catch (err) {
            loaderModal.message("<p>Could not load requirements</p><p>["+err+"]</p>",'error');
        }
    },
    stageThree : function(){
        loaderModal.message("Building interface");
        console.log("Building interface");
        
        //var outerBc = new dijit.layout.BorderContainer({
        //    "design": "headline",
        //    "style": "height: 100%;"
        //},
        //"uiContainer");
        //
        //// See here http://dtm.dijitheme.com/dijit
        //
        ///**
        // * Header
        //*/
        //var headerContent = new dijit.layout.ContentPane({
        //    "region": "top",
        //    "style": "height: 60px;"
        //});
        //headerContent.set('href','/tpl/header')
        //outerBc.addChild(headerContent);
        //
        ///**
        // * Inner Container
        //*/
        //var innerBc = new dijit.layout.BorderContainer({
        //    "design": "sidebar",
        //    "region": "center"
        //});
        //outerBc.addChild(innerBc);
        //
        ///**
        // * Footer
        //*/
        //var footerContent = new dijit.layout.ContentPane({
        //    "region": "bottom",
        //    "style": "height: 100px;",
        //    "splitter": "true"
        //});
        //outerBc.addChild(footerContent);
        //
        ///**
        // * Left container
        //*/
        //var leftSidebar = new dijit.layout.ContentPane({
        //    "region": "leading",
        //    "style": "width: 200px;",
        //    "splitter": "true",
        //    "content": "<button id='progButtonNode' type='button'></button>"
        //});
        //innerBc.addChild(leftSidebar);
        //// http://robrobbins.info/?p=372
        //var button = new dijit.form.Button({
        //    //label: "Click me!",
        //    iconClass:"dijitIcon plusIcon",
        //    showLabel: false,
        //    onClick: function() {
        //        // Do something:
        //        //dojo.byId("result1").innerHTML += "Thank you! ";
        //    }
        //},
        //"progButtonNode");
        ////leftSidebar.addChild(button);
        //
        //
        ///**
        // * Main Content
        //*/
        //var mainContent = new dijit.layout.BorderContainer({
        //    "id": "uiContent",
        //    "region": "center"
        //});
        //innerBc.addChild(mainContent);
        //
        ////rightContent.startup();
        //outerBc.startup();
        
        var infraStore = new dojo.data.ItemFileReadStore({url:"/imictl/get/infrastructures"});
        
        var model = new dijit.tree.ForestStoreModel({
            store: infraStore,
            query: {id: '*'},
            rootLabel: "Infrastructures"
            //onNewItem: function(item, parentInfo){
            //        if(this.store.getValue(item, 'type') == 'continent'){
            //                this._requeryTop();
            //        }
            //        this.inherited(arguments);
            //}
        });
        
        tree = new dijit.Tree({
            model: model
            
        });
        
        dijit.byId('uiLeftBarContainer').addChild(tree);
        
        
        //console.log(infraStore);
        this.fin();
    },
    fin : function(){
        loaderModal.done();
    }
    
}

/**
 * Modal loader window
 *
 * This is built in raw javascript (with no help from libraries) so it can be
 * used while those libraries are loading.
 *
 * @todo The window resize event does not work
*/
loaderModal = {
    div : "loading-mask",
    element : null,
    css  : "#loading-mask{background: #161616;filter:alpha(opacity=85);-moz-opacity:0.85;-khtml-opacity: 0.85;opacity: 0.85;visibility: hidden;position: absolute;left:0px;top:0px;width:100%;height:100%;text-align:center;z-index: 1000;}#loading-window{position:relative;background:#ddd;width:350px;height:175px;padding:10px;-moz-border-radius:5px;-webkit-border-radius:5px;}.loading-indicator{margin-top: 5px;}.loading-indicator img{width:32px;height:32px;margin-right:8px;}#loading-message{margin-top: 20px;overflow-y:auto;height: 120px;}",
    html : "<div id='loading-window'><div class='loading-indicator'><img src='http://media.lapinlabs.com/img/loader_01.gif' align='absmiddle' />Booting IMI&hellip;</div><div id='loading-message'></div></div>",
    load : function(options){
        // Build the element if it is missing
        if (!this.element) this._getElement();
        
        // Set the message
        if (typeof options != 'undefined' && typeof options.message != 'undefined')
            this.message(options.message);
        
        // Show the loader
        this.element.style.visibility="visible";
    },
    done: function(){
        if (!this.element) this._getElement();
        this.element.style.visibility="hidden";
    },
    message: function(msg,type){
        if (typeof type != 'undefined' && type == 'error'){
            var img = document.getElementById('loading-window').getElementsByTagName('img')[0];
            img.nextSibling.textContent = "ERROR";
            img.src = 'http://media.lapinlabs.com/img/exclamation.png';
        }
        document.getElementById('loading-message').innerHTML = msg;
    },
    _options : {
      
    },
    _onWindowSizeUpdate : function(){
        var loadingWindow = document.getElementById('loading-window');
        pos = this._center();
        loadingWindow.style.left = (pos[0] - Math.floor(loadingWindow.offsetWidth/2)) + "px";
        loadingWindow.style.top  = (pos[1] - Math.floor(loadingWindow.offsetHeight/2)) + "px";
    },
    _getElement: function(){
        var e = document.getElementById(this.div);
        if (typeof e != 'undefined' && e){
            this.element = e
        } else {
            loaderDiv = document.createElement('div');
            loaderDiv.setAttribute('id','loading-mask');
            loaderDiv.innerHTML = this.html;
            loaderStyle = document.createElement('style');
            loaderStyle.setAttribute('type','text/css');
            loaderStyle.innerHTML = this.css;
            document.body.appendChild(loaderStyle);
            document.body.appendChild(loaderDiv);
            this.element = loaderDiv;
        } 
        
        // Atach handler to window resize
        window.onresize = this._onWindowSizeUpdate;
        
        // Fire resize to center
        this._onWindowSizeUpdate();
        
        return e;
    },
    _center : function(){
        function getScreenCenterY() {
            var y = 0;
            y = getScrollOffset()+(getInnerHeight()/2);
            return(y);
        }
        function getScreenCenterX() {
            return(document.body.clientWidth/2);
        }
        function getInnerHeight() {
            var y;
            // all except Explorer
            if (self.innerHeight) y = self.innerHeight;
            // Explorer 6 Strict Mode
            else if (document.documentElement && document.documentElement.clientHeight)
                y = document.documentElement.clientHeight;
            // other Explorers
            else if (document.body) y = document.body.clientHeight;
            return(y);
        }
        function getScrollOffset() {
            var y;
            // all except Explorer
            if (self.pageYOffset) 
                y = self.pageYOffset;
            // Explorer 6 Strict
            else if (document.documentElement && document.documentElement.scrollTop)
                y = document.documentElement.scrollTop;
            // all other Explorers
            else if (document.body) y = document.body.scrollTop;
            return(y);
        }
        posY = getScreenCenterY();
        posX = getScreenCenterX();   
        return [posX,posY];
    }
}



