#!/usr/bin/node
if (process.argv.length === 2) {
	return (console.log('No argument'));
} else if (process.argv.length === 3) {
	return (console.log('Argument found'));
} else {
	return (console.log('Arguments found'));
}
