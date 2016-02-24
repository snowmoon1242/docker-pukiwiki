#!/usr/bin/perl
use XML::FeedPP;
use CGI;

$q = new CGI;

my $feedurl;
$feedurl = "YOUR_OWN_FEED_URL";

if($feedurl){
        my $feed;
        $feed = XML::FeedPP::RSS->new(); # for RSS

        $feed->merge($feedurl);

        print "Content-Type: text/xml\n\n";
        print $feed->to_string("UTF-8");
}else{
        print "Content-Type: text/xml\n\n";
        print "<xml></xml>";
}
