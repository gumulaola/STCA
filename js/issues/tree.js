function TreeNode(val) {
  this.val = val;
  this.left = null;
  this.right = null;
}

function buildTree(arr) {
  let rootVal = arr[0];
  let root = new TreeNode(rootVal);
  let queue = [root];
  let i = 1;

  while (queue.length) {
    let cur = queue.shift();
    if (arr[i] != null) {
      cur.left = new TreeNode(arr[i]);
      queue.push(cur.left);
    }
    i++;
    if (arr[i] != null) {
      cur.right = new TreeNode(arr[i]);
      queue.push(cur.right);
    }
    i++;
  }

  return root;
}

let input = [7, 3, null, 5, 6];

let root = buildTree(input);

function dfs(root) {
  if (!root) {
    return;
  }

  dfs(root.left);
  console.log(root.val);
  dfs(root.right);
}

dfs(root);

function toNums(root) {
  let res = [];
  let queue = [root];

  while (queue.length) {
    let cur = queue.shift();
    if (cur) {
      res.push(cur.val);
      queue.push(cur.left);
      queue.push(cur.right);
    } else {
      res.push(null);
    }
  }

  return res;
}

console.log(toNums(root));

let secondRoot = buildTree(toNums(root));

console.log(toNums(secondRoot));
