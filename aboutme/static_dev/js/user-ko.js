function Book(name, author, subject) {
    var self = this;
    self.name = ko.observable(name);
    self.author  = ko.observable(author);
    self.subject = ko.observable(subject);

    self.abbr = ko.computed(function(){
        return self.subject().short;
    });
}

function ProfileViewModel() {
    var self = this;

    self.tabs = ['Profile', 'Books'];
    self.selectedTab = ko.observable();
    self.selectedTabData = ko.observable();

    self.firstName = ko.observable('');
    self.lastName = ko.observable('');
    self.email = ko.observable('');

    self.selectTab = function(tab) {
        self.selectedTab(tab);
        location.hash = tab;
        if(tab == 'Profile') {
            $.getJSON("/users/ajax/info", {tab : tab},
                function(data) {
                    self.firstName(data.fname);
                    self.lastName(data.lname);
                    self.email(data.email);
                });
        }
    };

    // Full Name
    self.fullName = ko.computed(function() {
        var fname = self.firstName().charAt(0).toUpperCase() + self.firstName().slice(1);
        var lname = self.lastName().charAt(0).toUpperCase() + self.lastName().slice(1);
        return fname + " " + lname;
    }, self);

    self.updateProfile = function() {
        $.ajax("/users/ajax/info", {
            type: "post",
            contentType: "application/json",
            data: { fname: self.firstName, lname: self.lastName, email: self.email},
            error: function(result) { alert(result) }
        });
    };

    // Books
    self.subjects = [
        { name:'Algorithms', short: 'ADA'},
        { name:'C Programming', short:'C'}
    ];

    self.books = ko.observableArray([
        new Book('ADA', 'Coreman', self.subjects[0]),
        new Book('Let Us C', 'Yashwant Kanetkar', self.subjects[1])
    ]);

    self.addBook = function() {
        self.books.push(new Book('Sample Book', 'Sample Author', self.subjects[1]));
    };

    Sammy(function() {
        this.get('#tab', function(tab) {
            self.selectedTab(tab);
            if(tab == 'Profile') {
                $.getJSON("/users/ajax/info", {tab : tab},
                    function(data) {
                        self.firstName(data.fname);
                        self.lastName(data.lname);
                        self.email(data.email);
                    });
            }
        });
    }).run();
}

ko.applyBindings(new ProfileViewModel());
